
numero = int(input("Digite um número de 3 dígitos:"))
unidade = (numero // 100)
dezena = (numero // 10) - (unidade * 10)
centena = (numero // 1) - (unidade *100) - (dezena * 10)
soma = (centena + dezena + unidade)
if numero < 0:
    print("Número invalido!")
else:
    print("A soma dos 3 algarismos é:",soma)
