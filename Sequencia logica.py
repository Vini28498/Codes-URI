N=int(input())
j=1
k=1
j2=0
k2=0
for i in range(1, N+1):
    j=i*i
    k=i*j
    j2=j+1
    k2=k+1
    print("%i %i %i" %(i, j, k))
    print("%i %i %i" %(i, j2, k2))
