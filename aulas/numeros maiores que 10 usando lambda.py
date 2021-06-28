listanum = []
i = 0

def achar(lis):

    maior10 = list(filter(lambda x: x > 10, lis))

    return maior10


print("{***********}""\n  Bem vindo""\n{***********}")

while (True):
    


    listanum.append(int(input("digite o numero que deseja adicionar a lista: ")))

    if(listanum[i] == 0):
        maiores = achar(listanum)
        break
    
    print(listanum[i])
    i += 1
    


print(f"\n\nOs numeros maiores que 10 são {maiores} ")