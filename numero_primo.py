n=int(input('ingrese un numero: '))
c=1
for i in range(1,n):
    if n%i==0:
        c=c+1    
if c==2:
    print(f'el numero: {n}, es primo')
else:
    print(f'el nuemro: {n}, no es primo')
    