#generar la serie: (2x^3)/4! - (4x^5)/6! + (6x^7)/8! - (8x^9)/10! para n terminos y obtener la sumatoria 
n=int(input('ingrese un numero: '))
#k=int(input('numero de repeticiones del mismo numero: '))
t=0
for i in range(0,n): # se puede cambiar 0 por K 
    print(t)
    if i%2==0:
        t=t+1
    else:
        t=t-1
        