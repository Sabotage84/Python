import os
import random

workdir = os.getcwd()
files = os.listdir(workdir)
files.remove("renamer.py")
files_count = len(files)
new_names = list(range(1,files_count+1))
random.shuffle(new_names)

for x in range(files_count):
	extention = str(files[x])
	new_name = str(new_names[x])+extention[-4:]
	os.rename(files[x], new_name)
