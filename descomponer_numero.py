n=int(input("ingrese un numero: "))
m=n
for i in range(0,len(str(n))):
    n=n%10**(len(str(n)))
    print(n)