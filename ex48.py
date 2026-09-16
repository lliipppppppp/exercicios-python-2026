for num in range(10):
  n = int(input(f"Digite o {num+1} número inteiro: "))
par = 0
imp = 0

if (n % 2 == 0):
    par += 1
else:
    imp += 1

print(f"Os numeros pares são: {par}\nE os numeros impares são: {imp}")