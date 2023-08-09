"""moduleguard - Guard import(s) from IDLE interfering with system path."""

# Programmed by CoolCat467

from __future__ import annotations

__title__ = "moduleguard"
__author__ = "CoolCat467"
__license__ = "GPLv3"
__version__ = "0.0.0"

import json
import os
import sys
from collections.abc import Iterable
from types import TracebackType
from typing import Self


def does_path_interfere(
    path: str,
    modules: set[str],
    ignorepaths: set[str] | None = None,
) -> bool:
    """Return True if path contains something that could interfere."""
    if ignorepaths is None:
        ignorepaths = set()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        # Remove directories we have already visited
        for dirname in tuple(dirnames):
            if os.path.join(dirpath, dirname) in ignorepaths:
                dirnames.remove(dirname)

        for filename in filenames:
            # Skip filenames with no extension
            if os.path.extsep not in filename:
                continue
            # If filename is module name, bad
            if filename.split(os.path.extsep, 1)[0] in modules:
                return True

        # If this is a module internal directory
        if "__init__.py" in filenames:
            # Get the next level up's name and the module name
            level_up, dir_module_name = os.path.split(path)
            # If module name matches, bad
            if dir_module_name in modules:
                return True
            # We have checked this folder now
            # No need for next iteration to do so again
            ignorepaths.add(path)
            return does_path_interfere(level_up, modules, ignorepaths)
    # If nothing matched we should be fine
    return False


class ImportGuardContextManager:
    """Guard imports against user packages from idle's sys.path manipulation."""

    __slots__ = ("modules", "original")

    def __init__(self, modules: set[str]) -> None:
        """Initialize modules set."""
        self.modules = modules

    def __enter__(self) -> Self:
        """Remove interference."""
        # Get deep copy
        self.original = json.loads(json.dumps(sys.path))

        # Remove blanks
        index = 0
        while index < len(sys.path):
            if not sys.path[index]:
                sys.path.pop(index)
                continue
            index += 1

        if "idlelib" not in sys.modules:
            # We are in before IDLE, we should be safe
            return self

        # Remove conflict(s)
        max_read = 0
        for max_read, path in enumerate(sys.path):  # noqa: B007
            if path.startswith(sys.exec_prefix):
                break

        index = 0
        while index < max_read:
            if does_path_interfere(sys.path[index], self.modules):
                sys.path.pop(index)
                continue
            index += 1

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Restore sys.path."""
        sys.path.clear()
        for item in self.original:
            sys.path.append(item)


def guard_import(module_name: str) -> ImportGuardContextManager:
    """Guard import against user packages from idle's sys.path manipulation."""
    return ImportGuardContextManager({module_name})


def guard_imports(module_names: Iterable[str]) -> ImportGuardContextManager:
    """Guard imports against user packages from idle's sys.path manipulation."""
    return ImportGuardContextManager(set(module_names))


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
