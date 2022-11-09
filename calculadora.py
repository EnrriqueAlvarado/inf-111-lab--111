a=int(input("ingresar un numero: "))
b=int(input("ingresar un numero: "))

sum = a+b
res = a-b 
pro = a*b
div = a/b
div_en = a//b
mod=a%b
print(f'''
    la suma es: {sum}
    la resta es: {res}
    la multiplicacion es: {pro}
    la divicion es: {div}
    la divicion entera es: {div_en}
    el modulo es : {mod}
''')
