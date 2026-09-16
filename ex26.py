n1 = int(input("Digite um numero maior que 0: "))
n2 = int(input("Digite um expoente: "))


if (n1 and n2 > 0 and n2 <= 10):
   print(f"O resultado é: {n1 ** n2}")

else:
  print("Os numeros não são maiores que 0 ou o expoente e maior que 0.")