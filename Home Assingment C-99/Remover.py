import os
import shutil
import time

def remover():

    folderCounter = 0
    fileCounter = 0
    path = input('Enter the directory path:')
    days = 20
    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= getAge(root_folder):
                removeFolder(root_folder)
                folderCounter+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(root_folder, folder)
                    if seconds >= getAge(folderPath):
                        removeFolder(folderPath)
                        folderCounter+=1
        for file in files:
            filePath = os.path.join(root_folder, file)
            if seconds >= getAge(filePath):
                removeFile(filePath)
                fileCounter+=1

        else:
            if seconds>= getAge(path):

                removeFile(path)
                fileCounter+=1
                
    else:
        print(f"{path} not found")

    print(f"Total folder deleted {folderCounter}")
    print(f"Total files deleted {fileCounter}")


def removeFolder(path):

    if not shutil.rmtree(path):
        print(f" {path} is removed successfully")

    else:
        print(f"Unable to remove {path}")

def removeFile(path):

    if not os.remove(path):
        print(f" {path} is removed successfully")

    else:
        print(f"Unable to remove {path}")

def getAge(path):

    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == "__main__":
    remover()






            

