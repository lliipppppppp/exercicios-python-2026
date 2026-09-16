salario = float(input("Digite seu salário: "))
aumento = float(input("Digite seu percentual de aumento: "))
resul = 0

resul = (aumento / 100 + 1) * salario

print(f"O seu aumento foi de {resul}")