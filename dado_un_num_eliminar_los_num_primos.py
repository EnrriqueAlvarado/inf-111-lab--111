import math
n=int(input("ingrese un numero: "))
cd=int(math.log10(n))+1#cd cantidad de digitos
m=n
k=n
#while n>0:
#    print(n//10**(cd-1))
#    n=n%10**(cd-1)
#    cd=cd-1
# ---- voltear un numero y quitar los numeros primos
#for i in range(1,cd+1):
#    k=n%10
#    n=n//10
#    if k!=2 and k!=3 and k!=5 and k!=7:
#        print(k, end='' )
for i in range(1,cd+1):
    n=m                 #si n = 123
    n=n//10**(cd-1)    #123//10**(2)=1
    n=n%100
    print(n)
       