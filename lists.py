import random


list = []
for i in range (10) :
    list.append(random.randrange(1, 999))
print (list)

question= input("pick a number from the list")
number= int(question)
question2= input("Pick another number from the list")
number2= int(question2)

x= number
y= number2

def Maximum_Number(number, number2):
	if(x < y):
		return y
	else:
		return x
print("The bigger number is....")
print(Maximum_Number(number, number2))
