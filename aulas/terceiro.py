x = 15

while(True):
    for i in range(2, 16):

        if(x%i!=0):
            break

    if(i == 15):
        print(f"o numero {x} é divisivel pelso numeros de 1 a 15")
        break

    x+=1
