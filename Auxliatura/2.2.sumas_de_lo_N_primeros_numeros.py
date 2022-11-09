n=int(input('ingrese un numero: '))
s=0
for i in range(1,n+1):
    s=s+i
    if i==n:
        print(f'{i}={s}')
    else:
        print(i,end = "+")
