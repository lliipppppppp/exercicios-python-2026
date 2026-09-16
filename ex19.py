n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o segundo numero e aguarde a ordem Decrescente...  "))
o1 = 0
o2 = 0
o3 = 0

if (n1 >= n2 and n1 >= n3):
 o1 = n1
 if (n2 >= n3):
    o2 = n2
    o3 = n3
 else:
    o2 = n3
    o3 = n2
# ____________________________________________
elif (n2 >= n1 and n2 >= n3):
  o1 = n2
  if (n1 >= n3):
    o2 = n1
    o3 = n3
  else:
    o2 = n3
    o3 = n1
# ____________________________________________
else:
  o1 = n3
  if(n1>=n2):
   o2 = n1
   o3 = n2
  else:
   o2 = n2
   o3 = n1
print (o1, o2, o3)