# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Carlos Alberto
media_das_notas = 0
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))

soma_das_notas = nota1 + nota2 + nota3 + nota4
media_das_notas = soma_das_notas / 4

print("A média foi: " + str(media_das_notas))