
numero_1 = int(input("Digite o 1° número:"))
numero_2 = int(input("Digite o 2° número:"))
numero_3 = int(input("Digite o 3° número:"))
ordem = input("Digite 3 números e coloque (d) para decrescente e (c) para crescente:")
if ordem == "c" or ordem == "C" or ordem == "d" or ordem== "D":
    if ordem == "c" or ordem == "C":
        if numero_1 < numero_2 < numero_3:
            print(numero_1, numero_2, numero_3)
            
        elif numero_3 < numero_1 < numero_2:
            print(numero_3, numero_1, numero_2)
            
        elif numero_2 < numero_3 < numero_1:
            print(numero_2, numero_3, numero_1)
            
        elif numero_1 < numero_3 < numero_2:
            print(numero_1, numero_3, numero_2)
            
        elif numero_3 < numero_2 < numero_1:
            print(numero_3, numero_2, numero_1)

        elif numero_2 < numero_1 < numero_3:
            print(numero_2, numero_1,  numero_3)
            
    elif ordem == "d" or ordem == "D":
        if numero_1 > numero_2 > numero_3:
            print(numero_1, numero_2, numero_3)

        elif numero_2 > numero_3 > numero_1:
            print(numero_2, numero_3, numero_1)

        elif numero_2 > numero_3 > numero_1:
            print(numero_2, numero_3, numero_1)

        elif numero_1 > numero_3 > numero_2:
            print(numero_1, numero_3, numero_2)

        elif numero_3 > numero_2 > numero_1:
            print(numero_3, numero_2, numero_1)

        elif numero_2 > numero_1 > numero_3:
            print(numero_2, numero_1, numero_3)

            
        
    
