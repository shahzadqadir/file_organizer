from sys import argv
from pathlib import Path
from termcolor import colored

def list_dir(dir_name: Path):
    files_and_dirs = {}
    files_and_dirs['files'] = []
    files_and_dirs['dirs'] = []
    for entry in dir_name.iterdir():
        if entry.is_file():
            if entry not in files_and_dirs['files']:
                files_and_dirs['files'].append(entry.name)            
        else:
            if entry not in files_and_dirs['dirs']:
                files_and_dirs['dirs'].append(entry.name)
    return files_and_dirs

def main():
    base_dir = '.'
    if len(argv) > 1:
        base_dir = argv[1]

    entries = Path(base_dir)
    content = list_dir(entries)
    files, dirs = content['files'], content['dirs']
    if files:
        for file in files:
            print(file, end=' ')
    if dirs:
        for dir in dirs:
            print(colored(dir, 'green'), end=' ')
    print()

if __name__ == "__main__":
    main()