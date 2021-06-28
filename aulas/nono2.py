pala = input("palavra: ")

lisconf = []
for i in range(len(pala)):

    if(pala[i] not in lisconf):
        lisconf.append(pala[i])
    
    else:
        print("a palavra tem letras repetidas")
        break

if(i == (len(pala))):
    print("palavra não tem letras repetidas")
