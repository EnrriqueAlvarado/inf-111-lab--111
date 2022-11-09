'''8.Dado un numero N imprimir cuantos bits encendidos en su
 representacion binaria tine dicho numero'''
n=int(input("ingrese un numero: "))
binario=""
while n > 0:
    r=int(n%2)
    n=int(n/2)
    binario=str(r)+binario
print(f'binario: {binario}')
c=0
for i in range(len(binario)):
    if binario[i]=="1":
        c+=1
print(f'bits encendidos: {c}')