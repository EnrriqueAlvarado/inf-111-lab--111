n=int(input('ingrese un numero: '))
for i in range(2,n):
    if n%i==0:
        if i == n//2:
            print(i)
        else:
            print(i, end=", ")
