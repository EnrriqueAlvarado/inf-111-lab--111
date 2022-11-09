n=int(input('ingrese el numero de terminos: '))
val=0 #el termino de imprecion
inc=1 #el incremento de 1 a 5 y decremento
lim=1 #el limite del numero de veces de decrementos
cnt=0 #contador de ...
k=int(input('el numero maximo: '))
for i in range(n):
    val=val+inc
    if(i==n-1):
        print(val)
    else:
        print(val,end = ", ")
    
    if(inc==-1):
        cnt=cnt+1
        if(k-lim==cnt):
            val=0
            inc=1
            cnt=0
            lim=lim+1
            if(lim==k):
                lim=1

    if(val==k):
        inc=-1
        cnt=0
