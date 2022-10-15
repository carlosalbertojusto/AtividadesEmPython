#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7 (h = altura)

#Carlos Alberto

sexo = int(input("Digite o seu sexo: 1. Masculino ou 2. Feminino: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

peso_ideal = (72.7 * altura) - 58 if sexo == 1 else (62.1 * altura) - 44.7

print("Peso: %.2f / Peso ideal: %.2f" %(peso,peso_ideal))