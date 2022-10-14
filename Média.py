n1,n2,n3,n4 = map(float,input().split())
media = ((n1*2)+(n2*3)+(n3*4)+(n4))/(10)
if(media >= 7):
    print("Media: %.1f"%media)
    print("Aluno aprovado.")
    
elif(media < 5.0):
    print("Media: %.1f"%media)
    print("Aluno reprovado.")
    
elif((media >= 5.0) and (media <= 6.9)):
    n_exame = float(input(""))
    print("Media: %.1f" %media)
    print("Aluno em exame.")  
    print("Nota do exame: %.1f"%n_exame)

    med_final = (n_exame + media) / 2
    if(med_final >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f"%med_final)
