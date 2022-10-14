import math
a,b,c = map(float,input().split())
delta = ((b*b)-(4*(a)*(c)))
if(delta >= 0):
    if((2*a) != 0):
        R1 = ((-b)+(math.sqrt(delta)))/(2*a)
        R2 = ((-b)-(math.sqrt(delta)))/(2*a)
        print("R1 = %.5f"%R1)
        print("R2 = %.5f"%R2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
