from random import randint
m = []
n = []
un = 0
dez = 0
cent = 0

for i in range(10):

    m.append([])

    for j in range(10):

        m[i].append(randint(0, 9))

for i in range(10):

    for j in range(10):
        
        print(m[i][j], end=" ".center(3))
    print()

print("*" * 50)
print("Verificação".center(50))

for i in range(3):

    num = int(input("Digite os números entre 100 e 999 POR FAVOR!!: "))
    
    if num < 100 or num > 999:
        print("Digito inválido")
    
    else:
        n.append(num)

print(f"Números digitados: {n}")

conf = []
ci = []
cj = []

for a in range(3):
    
    nu = n[a]

    un = nu%10
    int(nu/10)
    dez = nu%10
    int(nu/10)
    cent = nu
        
    
    
    countlinha = 0
    countcoluna = 0 
    repl = 0
    repc = 0

    for i in range(10):
        for j in range(10):

            if(repl == 0):#verificar linha

                if(m[i][j] == un):
                    repl += 1
                    countlinha += 1
                    conf.append(i,j)

                else:
                    repl = 0
                    countlinha = 0
                    conf = []

            elif(repl == 1):

                if(m[i][j] == dez):
                    repl += 1
                    countlinha += 1
                    conf.append(i,j)
                    
                else:
                    repl = 0
                    countlinha = 0
                    conf = []
            
            elif(repl == 2):

                if(m[i][j] == cent):
                    repl += 1
                    countlinha += 1
                    break
                    
                else:
                    repl = 0
                    countlinha = 0
                    conf = []

            
                    
                    
    
        if(repc == 2):
            ci.append(conf[0],conf[1])
            ci.append([i])
            cj.append(conf[2],conf[3])
            cj.append([j]) 

        break

    else:
        ci.append(n/a)
        cj.append(n/a)
        break

        for j in range(10):
            if(repc == 0):#verificar coluna

                if(m[i][j] == un):
                    repc += 1
                    countcoluna += 1
                    conf.append(j,i)

                else:
                    repc = 0
                    countcoluna = 0
                    conf = []

            elif(repc == 1):

                if(m[j][i] == dez):
                    repc += 1
                    countcoluna += 1
                    conf.append(j,i)

                else:
                    repc = 0
                    countcoluna = 0
                    conf = []
            
            elif(repc == 2):

                if(m[j][i] == cent):
                    repc += 1
                    countcoluna += 1
                    break

                else:
                    repc = 0
                    countcoluna = 0
                    conf = []
        if(repl == 2):
            ci.append(conf[2],conf[3])
            ci.append([j])
            cj.append(conf[0],conf[1])
            cj.append([i])