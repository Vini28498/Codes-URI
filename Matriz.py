#Criei uma função para Matriz.
def criamatriz (Matriz,l,c):
    for i in range(l):
        L=[]
        for j in range(c):
            X=int(input("Digite o elemento %i%i: "%(i,j)))
            L.append(X)
        Matriz.append(L)
    return Matriz

#Uma função para Somar as linhas da Matriz.
def Somalinha(Matriz,l,c,Total):
    Soma=0
    for y in range(l):
        for w in range(c):
            A=Matriz[y][w]
            Soma=Soma+A
        Total.append(Soma)
        Soma=0
    return Total

#Uma função para somar as colunas da Matriz.
def Somacoluna(Matriz,l,c,Total):
    Soma=0
    for h in range(l):
        for g in range(c):
            B=Matriz[g][h]
            Soma=Soma+B
        Total.append(Soma)
        Soma=0
    return Tc

#Uma função para somar a diagonal principal da matriz.
def SomaDP(Matriz,l,c,Total):
    Soma=0
    x1=0
    x2=1
    for d in range(l):
        for e in range(x1,x2):
            C=Matriz[d][e]
            Soma=Soma+C
        x1=x1+1
        x2=x2+1
    Total.append(Soma)
    return Tdp

#Uma função para somar a diagonal secundaria da matriz.
def SomaDS(Matriz,l,c,Total):
    Soma=0
    x1=c - 1
    x2=c
    for q in range(l):
        for p in range(x1,x2):
            D=Matriz[q][p]
            Soma=Soma+D
        x1=x1 - 1
        x2=x2-1
    Total.append(Soma)
    return Tds 

# E uma função para printar a matriz obtida.
def imprimematriz(Matriz):
    for k in range(l):
        print(Matriz[k])
    return None

#Aqui estão todos os dados para o funcionamento das funções acima.
#Criei uma lista Total para receber a somatoria dos elementos.
l=int(input("Digite o numero de linhas: "))
c=int(input("Digite o numero de colunas: "))
Matriz=[]
Matriz=criamatriz(Matriz,l,c)
imprimematriz(Matriz)
Soma = []
Tl=[]
Tc=[]
Tdp=[]
Tds=[]
Total=[]
Somal=Somalinha(Matriz,l,c,Total)
Somac=Somacoluna(Matriz,l,c,Total)
Somadp=SomaDP(Matriz,l,c,Total)
Somads=SomaDS(Matriz,l,c,Total)

#Comparação dos elementos
x = Total[0]
Beletimeaprova = l+c+2

for f in range(Beletimeaprova):
    if (Total[f]!=x):
        print("Não é um Quadrado Mágico!")
        break
else:
    print("É um Quadrado Mágico!!!")

#FIM ;)
    
    
    


