'''
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa 
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

pergun = ["a. Telefonou para a vítima?","b. Esteve no local do crime?","c. Mora perto da vítima?","d. Devia para a vítima?","e. Já trabalhou com a vítima?" ]
resp = []

for i in range(5):
    print(pergun[i])

    while(True):
        res = input("sua resposta: ").lower()
        
        if(res != 's' and res != 'n'):
            print("apenas s/n são respostas validas")
        elif(res == 's'):
            resp.append(res)
            break
        else:
            break

if(len(resp) == 2):
    print("você é suspeito")

elif(len(resp) > 2):
    print("você é cumplice")

elif(len(resp) == 5):
    print("você é assassino")

else:
    print("você é inocente")

input()