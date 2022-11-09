# generar la serie 1,2,2,3,3,3,4,4,4,4,5,5,5,5,5...
n=int(input('introdusca el numero de terminos: '))
m=1
l=1
p=1
i=0
for i in range(i,n):
    print(m)
    p += 1
    if p > l:
        l += 1
        m +=1
        p = 1