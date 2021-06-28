from random import randint

ma_i = int(input("qual o tamanho da matriz ? "))
ma_j = ma_i

x = ma_i**2 # o maior numero 

S = (ma_i+(ma_i**3))/2 # resultado de cada linha

# Criação da matriz pré feita
matriz = [0]*ma_i
for i in range(ma_i):
    matriz[i] = [0]*ma_j

# Colocando os valores na matriz
for i in range(ma_i):
    for j in range(ma_j):
        while(True):
            num = randint(1,x)
            conf = 0

            # conferir se repetiu numero
            for i in range(ma_i):
                for j in range(ma_j):
                    if(num != matriz[i][j]):
                        conf+=1

            if(conf == x):
                matriz[i][j] = num
                break
            # conferir se repetiu numero
# Colocando os valores na matriz

# print da matriz
for i in range(ma_i):
    for j in range(ma_j):
        print(matriz[i][j], end=' ')
    print()
# print da matriz