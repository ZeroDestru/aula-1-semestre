import random

matriz = []
vez = random.randint(5,6)

for i in range(vez):

    matriz.append([])

    for j in range(vez):
        matriz[i].append(random.randint(0,10))



for i in range(len(matriz)):

    for j in range(len(matriz[i])):
        
        if(matriz[i][j] == 4):
            print(f"o numero se encontra na posição i = {i} j = {j}")