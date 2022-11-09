a=int(input('ingrese a: '))
b=int(input('ingrese b: '))
c=int(input('ingrese c: '))

if a!=0:
    x1=(-b+(b**2 -4*(a*c))**(1/2))/(2 * a)
    x2=(-b-(b**2 -4*(a*c))**(1/2))/(2 * a)
    print(f'''
    primera respuesta x1:{x1}
    primera respuesta x2:{x2}
    ''')
else:
    print('no tiene solucion')