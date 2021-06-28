from random import randint
surpresa = []
megasena = []

for i in range(6):
    if i not in megasena:
        megasena.append(int(input("Digite números de 1 a 60:  ")))
megasena.sort()
print(megasena)

for i in range(6):
    if i not in surpresa:
        surpresa.append(randint(1, 60))
surpresa.sort()
print(surpresa)