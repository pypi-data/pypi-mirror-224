"""Client for mypy daemon mode - Modified version of mypy.dmypy.client.

This manages a daemon process which keeps useful state in memory
rather than having to read it back from disk on each run.
"""

# Modified by CoolCat467
# Original at https://github.com/python/mypy/blob/master/mypy/dmypy/client.py
# Original retrieved November 24th 2022
# Last updated to match original on March 11th 2023

# Mypy (and mypyc) are licensed under the terms of the MIT license,
# reproduced below.
#
#    The MIT License
#
#    Copyright (c) 2012-2022 Jukka Lehtosalo and contributors
#    Copyright (c) 2015-2022 Dropbox, Inc.
#
#    Permission is hereby granted, free of charge, to any person obtaining a
#    copy of this software and associated documentation files (the "Software"),
#    to deal in the Software without restriction, including without limitation
#    the rights to use, copy, modify, merge, publish, distribute, sublicense,
#    and/or sell copies of the Software, and to permit persons to whom the
#    Software is furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.

from __future__ import annotations

__title__ = "Mypy Daemon Asynchronous Client"
__license__ = "MIT"

import contextlib
import io
import json
import os
import time
from collections.abc import Sequence
from typing import Any, cast

import trio
from mypy.dmypy_os import alive as _alive, kill as _kill
from mypy.dmypy_server import (
    Server as _Server,
    daemonize as _daemonize,
    process_start_options as _process_start_options,
)
from mypy.ipc import IPCClient as _IPCClient, IPCException as _IPCException
from mypy.version import __version__


async def _receive(connection: _IPCClient) -> Any:
    """Receive JSON data from a connection until EOF.

    Raise OSError if the data received is not valid JSON or if it is
    not a dict.
    """
    async_connection = trio.wrap_file(cast(io.BytesIO, connection))
    bdata: bytes = await async_connection.read()
    if not bdata:
        raise OSError("No data received")
    try:
        data = json.loads(bdata.decode("utf8"))
    except Exception as e:
        raise OSError("Data received is not valid JSON") from e
    if not isinstance(data, dict):
        raise OSError(f"Data received is not a dict ({type(data)})")
    return data


class BadStatusError(Exception):

    """Exception raised when there is something wrong with the status file.

    For example:
    - No status file found
    - Status file malformed
    - Process whose process id is in the status file does not exist
    """


# Client-side infrastructure.


def _read_status(status_file: str) -> dict[str, object]:
    """Read status file.

    Raise BadStatusError if the status file doesn't exist or contains
    invalid JSON or the JSON is not a dict.
    """
    if not os.path.isfile(status_file):
        raise BadStatusError("No status file found")
    with open(status_file, encoding="utf-8") as file:
        try:
            data = json.load(file)
        except Exception as ex:
            raise BadStatusError("Malformed status file (not JSON)") from ex
    if not isinstance(data, dict):
        raise BadStatusError("Invalid status file (not a dict)")
    return data


def _check_status(data: dict[str, Any]) -> tuple[int, str]:
    """Check if the process is alive.

    Return (process id, connection_name) on success.

    Raise BadStatusError if something's wrong.
    """
    if "pid" not in data:
        raise BadStatusError("Invalid status file (no pid field)")
    pid = data["pid"]
    if not isinstance(pid, int):
        raise BadStatusError("pid field is not an int")
    if not _alive(pid):
        raise BadStatusError("Daemon has died")
    if "connection_name" not in data:
        raise BadStatusError("Invalid status file (no connection_name field)")
    connection_name = data["connection_name"]
    if not isinstance(connection_name, str):
        raise BadStatusError("connection_name field is not a string")
    return pid, connection_name


def get_status(status_file: str) -> tuple[int, str]:
    """Read status file and check if the process is alive.

    Return (process id, connection_name) on success.

    Raise BadStatusError if something's wrong.
    """
    data = _read_status(status_file)
    return _check_status(data)


async def request(
    status_file: str,
    command: str,
    *,
    timeout: int | None = None,
    **kwds: object,
) -> dict[str, Any]:
    """Send a request to the daemon.

    Return the JSON dict with the response.

    Raise BadStatusError if there is something wrong with the status file
    or if the process whose process id is in the status file has died.

    Return {'error': <message>} if an IPC operation or receive()
    raised OSError.  This covers cases such as connection refused or
    closed prematurely as well as invalid JSON received.
    """
    response: dict[str, str] = {}
    args = dict(kwds)
    args["command"] = command
    # Tell the server whether this request was initiated from a
    # human-facing terminal, so that it can format the type checking
    # output accordingly.
    args["is_tty"] = False
    args["terminal_width"] = 80
    bdata = json.dumps(args).encode("utf8")
    _, name = get_status(status_file)
    try:
        with _IPCClient(name, timeout) as client:
            async_client = trio.wrap_file(cast(io.BytesIO, client))
            await async_client.write(bdata)
            response = await _receive(client)
    except (OSError, _IPCException, ValueError) as err:
        return {"error": str(err)}
    return response


def is_running(status_file: str) -> bool:
    """Check if the server is running cleanly."""
    try:
        get_status(status_file)
    except BadStatusError:
        return False
    return True


async def stop(status_file: str) -> dict[str, Any]:
    """Stop daemon via a 'stop' request."""
    return await request(status_file, "stop", timeout=5)


async def _wait_for_server(status_file: str, timeout: float = 5.0) -> bool:
    """Wait until the server is up. Return False if timed out."""
    endtime = time.time() + timeout
    while time.time() < endtime:
        try:
            data = _read_status(status_file)
        except BadStatusError:
            # If the file isn't there yet, retry later.
            await trio.sleep(0.1)
            continue
        # If the file's content is bogus or the process is dead, fail.
        try:
            _check_status(data)
        except BadStatusError:
            return False
        return True
    return False


async def _start_server(
    status_file: str,
    *,
    flags: list[str],
    daemon_timeout: int | None = None,
    allow_sources: bool = False,
    log_file: str | None = None,
) -> bool:
    """Start the server and wait for it. Return False if error starting."""
    start_options = _process_start_options(flags, allow_sources)
    if (
        _daemonize(
            start_options,
            status_file,
            timeout=daemon_timeout,
            log_file=log_file,
        )
        != 0
    ):
        return False
    return await _wait_for_server(status_file)


async def restart(
    status_file: str,
    *,
    flags: list[str],
    daemon_timeout: int | None = 0,
    allow_sources: bool = False,
    log_file: str | None = None,
) -> bool:
    """Restart daemon (it may or may not be running; but not hanging).

    Returns False if error starting.
    """
    # Bad or missing status file or dead process; good to start.
    with contextlib.suppress(BadStatusError):
        await stop(status_file)
    return await _start_server(
        status_file,
        flags=flags,
        daemon_timeout=daemon_timeout,
        allow_sources=allow_sources,
        log_file=log_file,
    )


# Action functions


async def start(
    status_file: str,
    *,
    flags: list[str],
    daemon_timeout: int = 0,
    allow_sources: bool = False,
    log_file: str | None = None,
) -> bool:
    """Start daemon if not already running.

    Returns False if error starting / already running.
    """
    if not is_running(status_file):
        # Bad or missing status file or dead process; good to start.
        return await _start_server(
            status_file,
            flags=flags,
            daemon_timeout=daemon_timeout,
            allow_sources=allow_sources,
            log_file=log_file,
        )
    return False


async def status(
    status_file: str,
    *,
    timeout: int = 5,
    fswatcher_dump_file: str | None = None,
) -> dict[str, object]:
    """Ask daemon to return status."""
    return await request(
        status_file,
        "status",
        timeout=timeout,
        fswatcher_dump_file=fswatcher_dump_file,
    )


async def run(
    status_file: str,
    *,
    flags: list[str],
    timeout: int | None = None,
    daemon_timeout: int = 0,
    log_file: str | None = None,
    export_types: bool = False,
) -> dict[str, Any]:
    """Do a check, starting (or restarting) the daemon as necessary.

    Restarts the daemon if the running daemon reports that it is
    required (due to a configuration change, for example).
    """
    if not is_running(status_file):
        # Bad or missing status file or dead process; good to start.
        await _start_server(
            status_file,
            flags=flags,
            daemon_timeout=daemon_timeout,
            allow_sources=True,
            log_file=log_file,
        )
    response = await request(
        status_file,
        "run",
        timeout=timeout,
        version=__version__,
        args=flags,
        export_types=export_types,
    )
    # If the daemon signals that a restart is necessary, do it
    if "restart" in response:
        await restart(
            status_file,
            flags=flags,
            daemon_timeout=timeout,
            allow_sources=True,
            log_file=log_file,
        )
        response = await request(
            status_file,
            "run",
            timeout=timeout,
            version=__version__,
            args=flags,
            export_types=export_types,
        )
    return response


def kill(status_file: str) -> bool:
    """Kill daemon process with SIGKILL. Return True if killed."""
    pid = get_status(status_file)[0]
    try:
        _kill(pid)
    except OSError as ex:
        print(ex)
        return False
    return True


async def check(
    status_file: str,
    files: Sequence[str],
    *,
    timeout: int | None = None,
    export_types: bool = False,
) -> dict[str, Any]:
    """Ask the daemon to check a list of files."""
    return await request(
        status_file,
        "check",
        timeout=timeout,
        files=files,
        export_types=export_types,
    )


async def recheck(
    status_file: str,
    export_types: bool,
    *,
    timeout: int | None = None,
    remove: list[str] | None = None,
    update: list[str] | None = None,
) -> dict[str, Any]:
    """Ask the daemon to recheck the previous list of files.

    If at least one of --remove or --update is given, the server will
    update the list of files to check accordingly and assume that any other
    files are unchanged.  If none of these flags are given, the server will
    call stat() on each file last checked to determine its status.

    Files given in --update ought to exist.  Files given in --remove need not
    exist; if they don't they will be ignored.
    The lists may be empty but oughtn't contain duplicates or overlap.

    NOTE: The list of files is lost when the daemon is restarted.
    """
    if remove is not None or update is not None:
        return await request(
            status_file,
            "recheck",
            timeout=timeout,
            export_types=export_types,
            remove=remove,
            update=update,
        )
    return await request(
        status_file,
        "recheck",
        timeout=timeout,
        export_types=export_types,
    )


async def inspect(
    status_file: str,
    location: str,  # line:col
    show: str = "type",  # type, attrs, definition
    *,
    timeout: int | None = None,
    verbosity: int = 0,
    limit: int = 0,
    include_span: bool = False,
    include_kind: bool = False,
    include_object_attrs: bool = False,
    union_attrs: bool = False,
    force_reload: bool = False,
) -> dict[str, Any]:
    """Ask daemon to print the type of an expression."""
    return await request(
        status_file,
        "inspect",
        timeout=timeout,
        show=show,
        location=location,
        verbosity=verbosity,
        limit=limit,
        include_span=include_span,
        include_kind=include_kind,
        include_object_attrs=include_object_attrs,
        union_attrs=union_attrs,
        force_reload=force_reload,
    )


async def suggest(
    status_file: str,
    function: str,
    do_json: bool,
    *,
    timeout: int | None = None,
    callsites: bool = False,
    no_errors: bool = False,
    no_any: bool = False,
    flex_any: float | None = None,
    use_fixme: str | None = None,
    max_guesses: int | None = 64,
) -> dict[str, Any]:
    """Ask the daemon for a suggested signature."""
    return await request(
        status_file,
        "suggest",
        timeout=timeout,
        function=function,
        json=do_json,
        callsites=callsites,
        no_errors=no_errors,
        no_any=no_any,
        flex_any=flex_any,
        use_fixme=use_fixme,
        max_guesses=max_guesses,
    )


async def hang(status_file: str, *, timeout: int = 1) -> dict[str, Any]:
    """Hang for 100 seconds, as a debug hack."""
    if not isinstance(timeout, int):
        raise ValueError("Timeout must be an integer!")
    return await request(status_file, "hang", timeout=timeout)


def do_daemon(
    status_file: str,
    flags: list[str],
    daemon_timeout: int | None = None,
) -> None:
    """Serve requests in the foreground."""
    options = _process_start_options(flags, allow_sources=False)
    _Server(options, status_file, timeout=daemon_timeout).serve()
