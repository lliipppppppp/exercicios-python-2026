termo1 = 0
termo2 = 1
fib = 1
i = 2
seq = int(input("Digite um número para descobrir a sequência geradora do fib: "))

print(fib,end="\t")

for i in range(seq-1):
  fib = termo1 + termo2
  termo1 = termo2
  termo2 = fib

  print(fib, end="\t")