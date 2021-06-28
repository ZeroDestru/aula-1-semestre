from random import randint
n = []
megasena = []
i = 0
cont = 0
res = ["não foi dessa vez", "acertou 1 numero", "acertou 2 numeros", "acertou 3 numeros", "parabéns, fez uma QUADRA", "parabéns, fez uma QUINA", "parabéns, fez uma SENA"]

while(i < 6):

    nu = randint(1, 60)

    if nu not in n:
        
        n.append(nu)
        i+=1

print(n)

i = 0

while(i < 6):

    nu = int(input(f"digite os numeros que deseja jogar: \nnumero {i+1}/6: "))
    
    if(nu >= 1 or nu <= 60):
        if nu not in megasena:
    
            megasena.append(nu)
            i+=1

for i in range(6):

    for j in range(6):

       if(n[i] == megasena[j]):
            cont += 1


print(res[cont])