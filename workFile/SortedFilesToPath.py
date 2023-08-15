import os
#dirName = {"Video": [".mp4", ".wma"], "Image": [".bmp", ".jpg", ".jpeg"], "Text": [".txt", ".pdf", ".doc", ".docx"], "Bin": [".bin", ".exe"], "Archiv": [".rar", ".sfx"]}

def validationDir(directories: dict) -> None:
    for item in directories:
        if not os.path.isdir(item):
            os.mkdir(item)

def sortFiles(directories: dict) -> None:
    import pathlib
    keys = list(directories.keys())
    files = os.listdir()
    for item in files:
        extinsion = pathlib.Path(item).suffix.lower()
        for typeFile in keys:
            if extinsion in directories[typeFile]:
                os.replace(item, typeFile + "\\" + item)
                break