list1 = []

list1.append(1)
print(list1)

list1.append(4)
print(list1)

list1.extend([4,5,6,7,8,9,0])
print(list1)

import random 
name_string = input("Give the names separate by '.' ")
names = name_string.split(",")
print(names)
