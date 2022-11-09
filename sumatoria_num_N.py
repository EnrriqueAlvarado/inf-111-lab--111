n=int(input('ingrese el numero de terminos: '))
s=0
for i in range(n):
    s=s+i
    if(i==n):
        print(f'{i}={s}')
    else:
        print(i,end = "+")
