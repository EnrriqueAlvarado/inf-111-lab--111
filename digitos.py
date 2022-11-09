#Numero de digitos
n=int(input('ingrese un numero: '))
c=0
while n>0:
    n=n//10
    c += 1
print(f'el numero de digitos es: {c}')
