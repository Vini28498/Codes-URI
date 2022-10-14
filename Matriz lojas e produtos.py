def lista_lojas(l):
    for i in range(3):
        l.append(str(input("Digite o nome da cidade %i: " %(i+1))))
    return l

def lista_produtos(p):
    for i in range(3):
        linha =[]
        for j in range(1):
            p = l
        p.append(linha)
    return p

def matriz_valores(m):
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(float(input("Digite o valor custo da cidade  %i para a cidade %i :" %(i+1,j+1))))
        m.append(linha)
    return m

l =[]
lojas = lista_lojas(l)
p = []
produtos = lista_produtos(p)
m = []
valores = matriz_valores(m)

matriz = []
a = "Lojas:"
matriz.append(a)
matriz.append(lojas)

for i in range(3):
    linha = []
    a = produtos[i]
    linha.append(a)
    for j in range(3):
        v = valores[i][j]
        linha.append(v)
    matriz.append(linha)
    

linha_soma = []
for k in range(3):
    cont = 0 
    for j in range(3):
        a = valores[j][k]
        cont += a
    linha_soma.append(cont)
    
b = "Total:"
matriz.append(b)  
matriz.append(linha_soma)

for m in range(7):
    print(matriz[m])

valor_minimo = min(linha_soma)
for p in range(3):
    if(linha_soma[p] == valor_minimo):
        loja_melhor = i-1
print("A compra com menor valor do produtos serão na loja: %i, gastonado R$:%i" %(loja_melhor,valor_minimo))


