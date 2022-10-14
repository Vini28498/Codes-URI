n1 = int(input(""))
cont = 0
for i in range(n1,):
    if(n1 % 2 != 0):
        cont = cont + 1
        print(i)
    if((n1+i)%2 != 0):
        cont = cont + 1
        print(i)
    if(cont == 6):
        break
