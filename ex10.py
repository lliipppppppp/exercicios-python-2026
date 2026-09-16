l1 = float(input("Digite o  primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if (l1 == l2  == l3):
  print("O seu triangulo é Equilátero!! ")

elif (l1 == l2 or l1 == l3 or l2 == l1 or l2== l3 or l3 == l1 or l3 == l2):
  print("O seu triangulo é Isósceles!! ")

else:
  print("O seu triangulo é Escaleno!! ")