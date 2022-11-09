'''9. Determinar si un número es capicuo.'''
n=int(input("ingrese un numero: "))
m=n
c=0
while m>0:
    m=m//10
    c+=1 #c-> numero de digitos
'''if c%2==0:
    for i in range(1,c):
        izq=0; der=0
        der=n%10**(i)'''
for i in range(1,c):
    n=n//10**(c-1)