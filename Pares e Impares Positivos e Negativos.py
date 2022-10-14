a = []
cont_par = 0
cont_postivo = 0
cont_impar = 0
cont_negativos = 0
for i in range(5):
    a.append(int(input("")))
    if(a[i] % 2 == 0):
        cont_par = cont_par + 1
    if(a[i] % 2 != 0):
        cont_impar = cont_impar + 1
    if(a[i] > 0):
        cont_postivo = cont_postivo + 1
    if(a[i] < 0):
        cont_negativos = cont_negativos + 1
print(cont_par,"valor(es) par(es)")
print(cont_impar,"valor(es) impar(es)")
print(cont_postivo,"valor(es) positivo(s)")
print(cont_negativos,"valor(es) negativo(s)")
