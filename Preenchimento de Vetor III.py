N=[]
X = float(input("DIGITE UM NÚMERO: "))
for i in range(0, 100):
    N.append(X)
    N[i]=X
    X=(X/2)
    print("N[%i] = %.4f"%(i, N[i]))
