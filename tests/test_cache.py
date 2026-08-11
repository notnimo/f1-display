import os
from pathlib import Path

import fastf1

from src.config import enable_cache


def _list_cache_files(cache_dir):
    path = Path(cache_dir)
    if not path.exists():
        return []
    return sorted(str(p.relative_to(path)) for p in path.rglob("*") if p.is_file())


def testCachePopulation():
    enable_cache()
    cache_dir = Path("./.fastf1cache").resolve()
    print(f"Cache directory: {cache_dir} {'exists' if cache_dir.exists() else 'does not exist'}")

    first_run_files = _list_cache_files(cache_dir)
    print(f"Cache files before first run: {len(first_run_files)}")

    print("First run: requesting session and populating the cache...")
    first_session = fastf1.get_session(2023, "Monza", "R")

    first_run_files_after = _list_cache_files(cache_dir)
    print(f"Cache files after first run: {len(first_run_files_after)}")
    print(f"First run created cache files: {first_run_files_after[len(first_run_files):]}")

    print("Second run: requesting the same session again...")
    second_session = fastf1.get_session(2023, "Monza", "R")

    second_run_files_after = _list_cache_files(cache_dir)
    print(f"Cache files after second run: {len(second_run_files_after)}")

    if len(second_run_files_after) < len(first_run_files_after):
        raise SystemExit("Cache size shrank after the second run")

    print("First session object:", first_session)
    print("Second session object:", second_session)