n1 = float(input("Digite um numero "))
n2 = float(input("Digite o segundo numero "))
conta = input("Vai querer Soma (+) ou Subtração (-)? ")
resul = 0

if (conta == "-"):
  resul = n1 - n2
  print(resul)

else:
  resul = n1 + n2
  print(resul)