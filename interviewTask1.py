import random 
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum3=0
for x in my_list:
    sum3=sum3+x
    print(sum3)
print(sum3)
print(my_list)
r = int(input("Inpup number from1 to 20: "))
my_list.remove(r)
print(my_list)
sum1=0
for x in range(1,21):
    sum1=sum1+x
    print(sum1)
random.shuffle(my_list)
print(my_list)
sum2=0
for x in my_list:
    sum2=sum2+x
    print(sum2)
print(sum1)
print(sum2)
print("Deleted element:{0}".format(sum1-sum2))
input("End...")
