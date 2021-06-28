at = 0
ant2 = 0
ant = 0
prox = 1

while(at < 500):
    print(at, end=' ')
    
    if(at == 0):
        at+=prox
    else:
        ant2 = at
        at = ant+prox
        ant = ant2
    prox=at    
print(at, end=' ')

input()