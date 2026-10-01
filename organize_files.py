#!/usr/bin/python3
import os
from pathlib import Path

def organize_files(base_path: str):
    path = Path(base_path)
    files_by_extension = {}
    for file in path.iterdir():
        ext = file.suffix[1:]
        if ext not in files_by_extension:
            files_by_extension[ext] = []
            files_by_extension[ext].append(file.name)
        else:
            files_by_extension[ext].append(file.name)
    return files_by_extension

if __name__ == "__main__":
    path_str = '/home/script/working_with_files/data'
    base_path = Path(path_str)
    files = organize_files(path_str)
    for file in files:
        path = Path(f'{path_str}/{file}')
        try:
            path.mkdir()
            for item in files[file]:
                Path(f'{path_str}/{item}').replace(os.path.join(path, item))
        except Exception:
            continue

