#!/usr/bin/env python3
"""Validate or create the private directory TMPDIR names."""

import os
import stat
import sys


def private_temp_dir(path):
    if not path.startswith("/") or path == "/" or any(
        part in (".", "..") for part in path.split("/")
    ):
        raise ValueError("TMPDIR must be an absolute directory path below /")

    current = ""
    parts = [part for part in path.split("/") if part]
    for index, part in enumerate(parts):
        current += "/" + part
        try:
            info = os.lstat(current)
        except FileNotFoundError:
            if index != len(parts) - 1:
                raise ValueError(f"parent directory does not exist: {current}") from None
            try:
                os.mkdir(current, 0o700)
            except FileExistsError:
                pass
            info = os.lstat(current)
        if index != len(parts) - 1 and stat.S_ISLNK(info.st_mode) and info.st_uid == 0:
            continue  # a system link such as macOS /tmp -> /private/tmp: only root can repoint it
        if not stat.S_ISDIR(info.st_mode):
            raise ValueError(f"not a directory or is a symlink: {current}")

    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        if os.fstat(fd).st_uid != os.geteuid():
            raise ValueError(f"TMPDIR is not owned by this user: {path}")
        os.fchmod(fd, 0o700)
    finally:
        os.close(fd)
    return path.rstrip("/")


if __name__ == "__main__":
    try:
        print(private_temp_dir(sys.argv[1]))
    except (ValueError, OSError) as error:
        sys.exit(str(error))
