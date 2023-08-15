import os
def validationDir(directories: dict) -> None:
    for item in directories:
        if not os.path.isdir(item):
            os.mkdir(item)