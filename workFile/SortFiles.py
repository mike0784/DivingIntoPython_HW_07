import os
from random import randint, choice

#from giveName import give_name

def create_files(ext: str, directory: str = None, min_len: int = 6,
                 max_len: int = 30, min_size: int = 256,
                 max_size: int = 4096, count_files: int = 42):
    if not os.path.isdir(directory):
        os.makedirs(directory)

    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w',
                  encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size,
                                                                  max_size)])

            output.write(str(list_of_bytes))


def sort_files(directory: str or os.Path = 'test_dir'):
    os.chdir(directory)
    print(os.listdir())
    for file in os.Path(os.getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in os.listdir():
            os.mkdir(ext.upper())
        file.replace(f"{ext.upper()}\\{file.name}")