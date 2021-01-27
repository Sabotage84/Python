import os
import random
workdir = os.getcwd()
files = os.listdir(workdir)
files.remove("renamer.py")
files_count = len(files)
new_names=[]
if (str(files[0])=="z0"):
        for x in range(files_count):
                new_names.append("xx"+str(x))
elif (str(files[0])=="xx0"):
        for x in range(files_count):
                new_names.append("z"+str(x))
else:
        new_names2=[]
        for x in range(files_count):
                new_names2.append(str(x))
        random.shuffle(new_names2)
        for x in range(files_count):
                extention = str(files[x])
        new_name = str(new_names2[x])+extention[-4:]
        os.rename(files[x], new_name)
        for x in range(files_count):
                new_names.append("xx"+str(x))
        

random.shuffle(new_names)
for x in range(files_count):
        extention = str(files[x])
        new_name = str(new_names[x])+extention[-4:]
        os.rename(files[x], new_name)

