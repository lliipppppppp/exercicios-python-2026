dis = input("Qual disciplina deseja saber a média? ")
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Agora insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))
resul = 0

resul = (nota1 + nota2 + nota3 + nota4) / 4

if (resul >= 7):
  print (f"Aprovado! Sua nota foi {resul}")

else:
  print (f"reprovado! Sua nota foi {resul}")