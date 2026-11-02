#!/usr/bin/env python3
"""Validate or create the private directory supplied by a harness launcher."""

import os
import stat
import sys


def private_temp_dir(path):
    if not path.startswith("/") or path == "/" or any(
        part in (".", "..") for part in path.split("/")
    ):
        raise ValueError("HARNESS_TMPDIR must be an absolute directory path below /")

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
        if not stat.S_ISDIR(info.st_mode):
            raise ValueError(f"not a directory or is a symlink: {current}")

    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        if os.fstat(fd).st_uid != os.geteuid():
            raise ValueError(f"HARNESS_TMPDIR is not owned by this user: {path}")
        os.fchmod(fd, 0o700)
    finally:
        os.close(fd)
    return path


if __name__ == "__main__":
    try:
        print(private_temp_dir(sys.argv[1]))
    except (ValueError, OSError) as error:
        sys.exit(str(error))
