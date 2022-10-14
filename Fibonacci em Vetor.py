T=int(input())
Fib=[]
num1=0
num2=1
n=0
Fib.append(num1)
Fib.append(num2)
for i in range(2, 64):
    n=num1+num2
    Fib.append(n)
    num1=num2
    num2=n
for i in range(1, T+1):
    N=int(input())
    print("Fib(%i) = %i" %(N, Fib[N]))
