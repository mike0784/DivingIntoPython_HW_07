#from workFile import *
import workFile.SortedFilesToPath
import workFile.validationDir
#from SortFiles import sortFiles
dirName = {"Video": [".mp4", ".wma"], "Image": [".bmp", ".jpg", ".jpeg"], "Text": [".txt", ".pdf", ".doc", ".docx"], "Bin": [".bin", ".exe"], "Archiv": [".rar", ".sfx"]}

if __name__ == "__main__":
    workFile.validationDir.validationDir(dirName)
    workFile.SortedFilesToPath.sortFiles(dirName)