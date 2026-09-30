int0 = 0
int26 = 0
int51 = 0
int76 = 0

while n >= 0:
 n = int(input("Digite um número (numero negativo para encerrar o programa): "))



if (0 <= n or n <= 25): 
  int0 +=1

elif (26 <= n or 50 <= n):
  int26 +=1

elif (51 <= n or 75 <= n):
  int51 +=1

elif (76 <= n or 100 <= n):
  int76 +=1



print (f"O intervalo entre 0-25 é {int0}  \n")
print (f"O intervalo entre 26-50 é {int26} \n")
print (f"O intervalo entre 51-75 é {int51}  \n")
print (f"O intervalo entre 76-100 é {int76}  \n")
