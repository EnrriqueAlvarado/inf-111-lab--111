n=int(input("introdusca el numero de terminos: "))
c=1; k=2; p=2
while c<=n:
  if p%k!=0 and k<=p//2: #que el nro no tenga divisores distintos a 1 
    k=k+1 #incremento de del valor de la variable de divisor
  else:
    if k>p//2: #verificamos que sea primo
      print(p)
      c=c+1 #incrementamos el contador
    p=p+1 #buscamos el siguiente numero primo
    k=2 #valor inicial de divisores