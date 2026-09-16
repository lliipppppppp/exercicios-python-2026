salario = float(input("Digite seu salario: "))
gratif = 0
gratif = salario * 0.05
salario = salario + gratif
imposto = salario * 0.07
salario = salario - imposto


print(f"Seu salario é {salario}")
