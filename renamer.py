import os
import random
workdir = os.getcwd()
files = os.listdir(workdir)
files.remove("renamer.py")
files_count = len(files)
new_names=[]
if ("z" in str(files[0])):
	for x in range(files_count):
	    new_names.append("xx"+str(x))
else:
	for x in range(files_count):
	    new_names.append("z"+str(x))

random.shuffle(new_names)
for x in range(files_count):
	extention = str(files[x])
	new_name = str(new_names[x])+extention[-4:]
	os.rename(files[x], new_name)
