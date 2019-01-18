import random 
from random import randint

#my_list=list(range(1,80))
my_list = [randint(0, 9) for i in range(78)]
print (my_list)
random.shuffle(my_list)
print (my_list)
print()
print()
print()
for j in range(1,78):
	key=my_list[j]
	i=j-1
	while (i>=0 and my_list[i]>key):
		my_list[i+1]=my_list[i]
		print(my_list)
		i=i-1
	my_list[i+1]=key
	print()
	print (my_list)
	print()

print(my_list)

input("End...")
