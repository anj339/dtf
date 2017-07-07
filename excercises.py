#python excercises 
import math




answer = input("Side length 1?")
side= int(answer)
x=side
answer = input("Side length 2?")
side2= int(answer)
y=side2 
answer = input("Side length 3?")
side3= int(answer)
z= side3

def isScalene(x, y, z): 
	if (x>0 and y>0 and z>0):
		if (x!=y!=z):
			return True
		else:
			return False
		
	else:
		return False
		

print(isScalene(x, y, z))
	
	

