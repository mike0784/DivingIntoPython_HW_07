import os
def filterFiles(extension_old: str) -> list:
    import pathlib
    files = os.listdir()
    result = []
    for item in files:
        if pathlib.Path(item).suffix.lower() == extension_old:
            result.append(item)
    return result

def num(count_nums: int, count: int) -> str:
    return str(count).rjust(count_nums, "0")

def nameFormat(name: str, wanted_name: str, diapazon: list) -> str:
    return name[diapazon[0]:diapazon[1]] + wanted_name

def rename(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list) -> None:
    files = filterFiles(extension_old)
    print("Все файлы и папки", files)
    for i in range(0, len(files)):
        split_tt = os.path.splitext(files[i])
        newFile = nameFormat(split_tt[0], wanted_name, diapazon) + num(count_nums, i) + extension_new
        os.rename(files[i], newFile)


if __name__ == '__main__':
    rename(wanted_name = "video", count_nums=3, extension_old=".pdf", extension_new=".csv", diapazon=[3, 6])