nota_1 = float(input("Digite a 1° nota:"))
nota_2 = float(input("Digite a 2° nota:"))
nota_3 = float(input("Digite a 3° nota:"))
peso_1 = (nota_1 * 1)
peso_2 = (nota_2 * 1)
peso_3 = (nota_3 * 2)
mediaPonderada = ((peso_1 + peso_2 + peso_3) / 3)
if mediaPonderada >= 6:
    
    print("Aluno Aprovado!", mediaPonderada)
else:
    print("Aluno Reprovado!", mediaPonderada)
