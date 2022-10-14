cont=0
a = []
for i in range (6):
    a.append (int(float(input())))
    if(a[i]>0):
        cont = cont +1
print(cont,"valores positivos")
