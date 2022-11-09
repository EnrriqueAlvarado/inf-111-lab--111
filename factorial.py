# factorial de un numero n
n = int(input('ingrese un numero: '))
f = 1
i = 1
while i <= n:
    f = f * i
    i += 1
print(f'el factorial es: {f}')
