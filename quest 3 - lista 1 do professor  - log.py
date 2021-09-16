import math
numero = int(input("Digite um número inteiro:"))
logaritmo = math.log10(numero)
if numero < 0:
    print("Número invalido!")
else:
    print("o log de número é igual a:",logaritmo)
