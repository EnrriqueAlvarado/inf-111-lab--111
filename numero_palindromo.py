numero = int(input("numero : "))
if numero > 99 and numero < 999:
    print("el numero tiene tres cifras")
else:
    print("el numero no tiene tres cifras")

if numero//100==numero%10:
    print("el numero es palindromo")
else:
    print("el numero no es palindromo")
