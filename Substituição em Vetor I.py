X=[]
for i in range(10):
    n=int(input("Digite um número: "))
    X.append(n)
for i in range(10):
    if (X[i]<=0):
        X[i]=1
    print("X[%i] = %i" %(i, X[i]))
