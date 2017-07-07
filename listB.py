import random
import operator

list = []
for i in range (3):
    list.append(random.randrange(1, 999))
print (list)

x= list[0]
y= list[1]
z= list[2]

def Big_Number(x, y, z):
	if (x < y  and z < y):
		return y
	
	if (y < z and x < z):
			return z
	else:
		return x
		

print("and the biggest number is.......")	
print(Big_Number(x, y, z))