n = int(input("Digite um numero se quiser: "))

if (n <= 1):
  print("Não é um numero primo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
  primo = True
  for i in range(2, n):
      if(n % i == 0):
        primo = False
        break

if primo:
    print("È um numero primo")
else:
    print("O numero não é primo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")