X = int(input ())
for i in range (1, X+1):
    N=int(input())
    d=0
    for j in range(1, N+1):
        if N%j==0:
            d=d+1
    if d==2:
        print("%i eh primo"%N)
    else:
        print("%i nao eh primo"%N)
