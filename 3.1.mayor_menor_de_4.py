'''Escribir un programa para ingresar cuatro números enteros por teclado y a continuación
muestre en la pantalla el mayor de los cuatro números introducidos y también el menor de
ellos.

a=int(input())
b=int(input())
c=int(input())
d=int(input())'''
a, b ,c, d = map(int, input().split())

if (a>b and a>c and a>d):
    mayor=a
elif(b>a and b>c and b>d ):
    mayor=b
elif(c>a and c>b and c>d):
    mayor=c
else:
    mayor=d

if (a<b and a<c and a<d):
    menor=a
elif (b<a and b<c and b<d):
    menor=b
elif (c<a and c<b and c<d):
    menor=c
else:menor=d

print(f'{mayor} {menor}')