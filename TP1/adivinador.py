import random

def adivina (it):	
	for i in range(0, it):
		n = random.randint(0, 100)
		e = int(input("Ingrese el numero por " + str(i+1) + "º vez:   "))
		if (n == e):
			return str(i+1)	
	return "No lo ha logrado"
	
print (adivina(6))
