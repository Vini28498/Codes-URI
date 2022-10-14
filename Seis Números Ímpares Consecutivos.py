''' MANEIRA 1
a = []
cont_impar = 0
num = int(input())
for i in range (12):
    if(num % 2 != 0):
        a.append(num)
        cont_impar = cont_impar + 1
        num = num+1
        if(cont_impar == 6):
            print(a)
            break
    else:
        num = num +1'''

''' MANEIRA 2 '''
cont_impar = 0
num = int(input())
for i in range(13):
    if(num % 2 != 0):
        print(num)
        num = num + 1
        cont_impar = cont_impar + 1
        if(cont_impar == 6):
            break
    else:
        num = num + 1
