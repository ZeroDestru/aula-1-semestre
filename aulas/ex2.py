from random import randint
temp = []
maior = 0
media = 0
menor = 100
vezes = randint(5, 25)

while(True):
    temp.append(randint(-30, 67))
    if(vezes == len(temp)):
        break

for i in range(len(temp)):
    media+=temp[i]
    if(temp[i] > maior):
        maior = temp[i]
    if(temp[i] < menor):
        menor = temp[i]
media/=len(temp)

print(f"a maior temperatura já registarada é {maior}\na menor temperatura já registrada é {menor}\na média de temperaturas é {media:.0f}")

input()