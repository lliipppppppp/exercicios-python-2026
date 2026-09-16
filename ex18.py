valor = int(input("Insira o valor do seu depósito: "))
juros = int(input("Digite sua taxa de juros: "))
rend = (juros / 100)*valor
valorF = rend + valor

print(f"O rendimento é {rend} e o valor depois do rendimento é {valorF}")