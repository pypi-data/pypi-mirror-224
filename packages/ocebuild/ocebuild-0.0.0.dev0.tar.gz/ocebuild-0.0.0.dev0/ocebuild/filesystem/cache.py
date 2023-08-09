## @file
# Copyright (c) 2023, The OCE Build Authors. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
##
"""Methods for handling cross-platform file caching operations."""

from tempfile import gettempdir, mkdtemp, NamedTemporaryFile

from typing import Generator, List, Union

from .posix import remove

from ocebuild.parsers.regex import re_search

from third_party.cpython.pathlib import Path


def _iter_temp_dir(prefix: str,
                   dir_: Union[str, Path]
                   ) -> Generator[Path, any, None]:
  """Iterate over all temporary directories."""
  for d in Path(dir_).iterdir():
    if d.is_dir() and d.name.startswith(prefix):
      yield d

def _get_temp_dir(prefix: str="ocebuild-", clear: bool=False) -> Path:
  """Return the path to a directory that can be used for ephemeral caching.

  Args:
    prefix: The prefix to use for the temporary directory.
    clear: Whether to clear any existing cache directories.

  Returns:
    The path to the temporary directory.
  """
  cache_dirs = sorted(set(_iter_temp_dir(prefix, gettempdir())),
                      key=lambda d: -d.stat().st_ctime)
  # Remove all but the most recent cache directory
  if cache_dirs:
    for i,d in enumerate(cache_dirs):
      if i: remove(d)
    # Return the most recent cache directory
    tmpdir = next(iter(cache_dirs))
    if not clear:
      return Path(tmpdir)
    else:
      remove(tmpdir)
  # Create a new cache directory
  tmpdir = mkdtemp(prefix=prefix)
  return Path(tmpdir)

CACHE_DIR = _get_temp_dir(prefix="ocebuild-cache-")
"""Global cache directory for storing and re-using files between builds."""

UNPACK_DIR = _get_temp_dir(prefix="ocebuild-unpack-", clear=True)
"""Directory for unpacking and handling remote or cached archives."""

def clear_cache(cache_dirs: List[Path]):
  """Clears all cache directories"""
  if not cache_dirs:
    cache_dirs = (CACHE_DIR, UNPACK_DIR,)
  for cache_dir in cache_dirs:
    for path in cache_dir.iterdir():
      # Is generated by `tempdir._RandomNameSequence`
      if re_search(r'^tmp[a-z0-9_]{8}$', path.name):
        remove(path)


__all__ = [
  # Constants (2)
  "CACHE_DIR",
  "UNPACK_DIR",
  # Functions (1)
  "clear_cache"
]
