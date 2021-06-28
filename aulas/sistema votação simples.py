#O Brasil tem um grave problema quando falamos em política, 
# porém podemos ter ações que podem melhorar alguns dos fatores. 
# A primeira que teremos é criar um algoritmo base para a Urna Eletrônica. 
# Nesse algoritmo teremos apenas 5 canditados por enquanto:
#1 - Vincent Vega
#2 - Rick Dalton
#3 - Shoshanna Dreyfus
#4 - Beatrixx Kido
#5 - Jules Winnfield
#Vocês devem criar um algoritmo que pergunte quantos eleitores irão participar, 
# cada eleitor terá direito a apenas um voto, porém se realizar um voto errado 
# (um número de candidato que não existe), 
# tem 5 chances até informar um voto válido. 
# No final deve informar a porcentagem de votos de todos os candidatos e quem foi eleito.
# Não precisa considerar segundo turno. Caso ocorra um empate, 
# mostrar quais os nomes empatados e porcentagem de empate.

#Obs: o desafio é não usar listas na implementação

Vincent_Vega = 0
Rick_Dalton = 0
Shoshanna_Dreyfus = 0
Beatrixx_Kido = 0
Jules_Winnfield = 0
num = 0
ganhador = ''
ganhador1 = ''
ganhador2 = ''
ganhador3 = ''
ganhador4 = ''

elei = int(input("digite o numero dse eleitores que irão participar: "))
porct = 100//elei

#inicio de votação
for i in range(elei):
    print("\tBem Vindo a Urna Eletrônica\n\n\nescolha a opção de cadidato que deseja votar\n\tVincent Vega 10\n\tRick Dalton 21\n\tShoshanna Dreyfus 35\n\tBeatrixx Kido 44\n\tJules_Winnfield 77")
    
    for i in range(5):#inicio de tentativa de voto

        op = int(input("\ndigite a opção desejada: "))

        if(op == 10):
            Vincent_Vega += 1
            print("\nvoto computado com sucesso para Vincent Vega")
            break

        elif(op == 21):
            Rick_Dalton += 1
            print("\nvoto computado com sucesso para Rick Dalton")
            break
        
        elif(op == 35):
            Shoshanna_Dreyfus += 1
            print("\nvoto computado com sucesso para Shoshanna Dreyfus")
            break
        
        elif(op == 44):
            Beatrixx_Kido += 1
            print("\nvoto computado com sucesso para Beatrixx Kido")
            break
        
        elif(op == 77):
            Jules_Winnfield += 1
            print("\nvoto computado com sucesso para Jules Winnfield")
            break
        
        elif i == 4:
            print("\n\thouve erro 5 vezes\n\t\avoto inválido")
        
        else:
            print(f"\num número de candidato que não existe\n\tfalta {4-i} tentativas")
    #fim da tentativa de voto
#fim de otação

print(f"\nVincent Vega {Vincent_Vega*porct}%, Rick Dalton {Rick_Dalton*porct}%, Shoshanna Dreyfus {Shoshanna_Dreyfus*porct}%, Beatrixx Kido{Beatrixx_Kido*porct}%, Jules Winnfield{Jules_Winnfield*porct}%")

#inicio de definiçao de ganhador
if(Vincent_Vega >= Rick_Dalton and Vincent_Vega >= Shoshanna_Dreyfus and Vincent_Vega >= Beatrixx_Kido and Vincent_Vega >= Jules_Winnfield ):
    ganhador = "Vincent Vega"

if(Rick_Dalton >= Vincent_Vega and Rick_Dalton >= Shoshanna_Dreyfus and Rick_Dalton >= Beatrixx_Kido and Rick_Dalton >= Jules_Winnfield):
    ganhador1 = "Rick Dalton"

if(Shoshanna_Dreyfus >= Vincent_Vega and Shoshanna_Dreyfus >= Rick_Dalton and Shoshanna_Dreyfus >= Beatrixx_Kido and Shoshanna_Dreyfus >= Jules_Winnfield):
    ganhador2 = "Shoshanna Dreyfus"

if(Beatrixx_Kido >= Vincent_Vega and Beatrixx_Kido >= Rick_Dalton and Beatrixx_Kido >= Shoshanna_Dreyfus and Beatrixx_Kido >= Jules_Winnfield):
    ganhador3 = "Beatrixx Kido"

if(Jules_Winnfield >= Vincent_Vega and Jules_Winnfield >= Rick_Dalton and Jules_Winnfield >= Shoshanna_Dreyfus and Jules_Winnfield >= Beatrixx_Kido):
    ganhador4 = "Jules Winnfield"
#fim de definiçao de ganhador

#inicio de contagem de votos para ganhadores
if(len(ganhador) > 1):
    num += Vincent_Vega

if(len(ganhador1) > 1):
    num += Rick_Dalton

if(len(ganhador2) > 1):
    num += Shoshanna_Dreyfus

if(len(ganhador3) > 1):
    num += Beatrixx_Kido

if(len(ganhador4) > 1):
    num += Jules_Winnfield

porctem = 100//num
#fim de contagem de votos para ganhadores

#inicio de impressão de ganhadores
print("\tO(s) Candidato(s) eleito(s) ")
if(len(ganhador) > 1):
    print('\t',ganhador,end=' ')

    if(num > Vincent_Vega):
        print(f"porcentagem de empate {porctem*Vincent_Vega}")

if(len(ganhador1) > 1):
    print('\t',ganhador1,end=' ')

    if(num > Rick_Dalton):
        print(f"porcentagem de empate {porctem*Rick_Dalton}")

if(len(ganhador2) > 1):
    print('\t',ganhador2,end=' ')

    if(num > Shoshanna_Dreyfus):
        print(f"porcentagem de empate {porctem*Shoshanna_Dreyfus}")

if(len(ganhador3) > 1):
    print('\t',ganhador3,end=' ')

    if(num > Beatrixx_Kido):
        print(f"porcentagem de empate {porctem*Beatrixx_Kido}")

if(len(ganhador4) > 1):
    print('\t',ganhador4,end=' ')

    if(num > Jules_Winnfield):
        print(f"porcentagem de empate {porctem*Jules_Winnfield}")
#fim de impressão de ganhadores

input("pressione enter para sair: ")