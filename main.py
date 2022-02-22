import glob
from typing import Tuple
import os

fileList = glob.glob("./file/*")

print("1. Snake case -> Camel case")
print("2. Camel case -> Snake case")
MODE = int(input("입력 > "))

for file in fileList:
    fileName = file.split("./file\\")[1]
    oldName = fileName.split(".")[0]
    extension = fileName.split(".")[1]
    
    newName = ""

    isBeforeUnderbar = False
    for n, i in enumerate(oldName):
        if(MODE == 1):
            if(isBeforeUnderbar):
                newName += i.upper()
                isBeforeUnderbar = False
            elif (i == "_"):
                isBeforeUnderbar = True
                continue
            else:
                newName += i
        elif(MODE == 2):
            if(i.isupper()):
                if(n == 0):
                    newName += i.lower()
                else:
                    newName += "_" + i.lower()
            else:
                newName += i


    print(f"{file} -> {newName}.{extension}")
    os.rename(f"{file}", f"./result\{newName}.{extension}")