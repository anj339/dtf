

question= input("pick a start number ")
number= int(question)
question2= input("pick an end number ")
number2= int(question2)



list = [] 


def numbers(number, number2):
	while number <= number2:
		list.append(number)
		number = number + 1
			
	print(list)
	
numbers(number, number2)