num = int(input("escreva um numero: "))
confere = 0

for i in range(2, int(num/2)):
    
    print(num%i)

    if(num%i == 0):	#false	
	    confere = 1
	    break

if(confer__e == 1): #false
	print(f"{num} não é primo")
else:
	print(f"{num} é primo")



