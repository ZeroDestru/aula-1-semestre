'''
Baseado no último vídeo da aula passada, escreva uma função para implementar a ordenação Bubble Sort e teste com uma lista criada com 25 números aleatórios entre 1 e 50.

Atenção: Não utilize funções ou métodos prontos para ordenar os números.
'''

from random import randint

l = []

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False

    while not ordenado:

        ordenado = True
        
        for i in range(elementos):
        
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
        
    
    return lista

for i in range(25):
    l.append(randint(1, 50))

print(f"lista original : {l}")

l2 = bubble_sort(l)

print(f"lista ordenada : {l2}")