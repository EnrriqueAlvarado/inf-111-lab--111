#contar las vocales de una frase
f=input("ingrese una frase: ")
vocal=["a","e","i","o","u"]
c=0
for i in range vocal:
	for j in range f: 
		if(i==j):
			c=c+1
print(f'el numero de vocales es: {c}')

