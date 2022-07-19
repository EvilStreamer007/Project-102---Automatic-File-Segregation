import os 
import shutil

path = '/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-102'
source = '/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-102/assets'
destination = '/Users/chaitalishah/Desktop/Krsna_WHJ/Projects/Project-102/move_here'

list = os.listdir(source)

for count in list:
    name, extension = os.path.splitext(count)

    if extension == "":
        continue
    
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif', '.txt', '.doc', '.docx', '.pdf']:
        path1 = source + "/" + count
        path2 = destination + "/" + "Image OR Text Files"
        path3 = destination + "/" + "Image OR Text Files" + count

        if os.path.exists(path2):
            print("Moving file to",destination,"....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving file to",destination,"....")
            shutil.move(path1,path2)