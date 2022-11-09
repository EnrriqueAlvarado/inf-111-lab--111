n=int(input("introdusca el numero de terminos: "))
c=1; k=2; p=2
while c<=n:
  if p%k!=0 and k<=p//2:  
    k=k+1 
  else:
    if k>p//2: 
      print(p)
      c=c+1 
    if p==n-1:
        break 
    p=p+1
    k=2 