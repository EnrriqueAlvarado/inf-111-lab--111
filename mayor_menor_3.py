a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
c=int(input("ingrese el tercer numero: "))
if a>b:
    mayor=a
    menor=b
    if a>c:
        mayor=a
        if c<b:
            menor=c
        else:
            menor=b
    else:
        mayor=c
else:
    menor=a
    mayor=b
    if b>c:
        mayor=b
        if c<a:
            menor=c
    else:
        mayor=c
print(f'''
    el numero mayor es:{mayor}
    el numero menor es:{menor} 
''')