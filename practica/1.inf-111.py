'''1. Dados los lados de un rectángulo, calcular el área y el perímetro.'''
a, b = map(int, input("ingrese la altura y base: ").split())
area = a * b
perimetro = 2*(a+b)
print(f'area: {area}, perimetro: {perimetro}')