N=[]
V=int(input())
for i in range(10):
    N.append(V)
    V=V*2
    print("N[%i] = %i"%(i, N[i]))
