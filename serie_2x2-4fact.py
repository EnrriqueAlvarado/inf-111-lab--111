# sumatoria s=(2x^3)/4! - (4x^5)/6! + (6x^7)/8! - (8x^9)/10! ... para n terminos
n=int(input('ingrese el numero de terminos: '))
x=int(input('ingrese al variable: '))
a=0
for i in range(1,n):
    a=a+2
    b=x**(a+1)
    f=2+a
    fact=1
    for j in range(1,f):
        fact=fact*j
    num=a*b
    t=num/fact
    s=0
    if i%2==0:
        t=t*(-1)
    s=s+t
print(f'la sumatoria es {s}')