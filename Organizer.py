import os
import shutil

path = input("Enter the Path : ")
files = os.listdir(path)

for file in files :
    filename,extension = os.path.splitext(file)
    extension = extension[1:] #to Remove dot(.) from extension

    if os.path.exists(path + '/' + extension) :
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else :
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)