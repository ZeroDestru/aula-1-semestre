from random import randint
import time

L = []
t = []
tam = 5000

for i in range(10):

    

    for j in range(5000):

        L.append(randint(1, tam))
        ini = time.time()
        L.sort()
        fim = time.time()
    
    t.append(fim - ini)
    
    tam += 5000

tam = 5000
print("}--------------------tabela--------------------{")

for i in range(10):
    print(f"   Tamanho: {tam} >> Tempo: {t[i]}")
    print("}----------------------------------------------{")
    tam += 5000