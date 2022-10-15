# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e apresentar:
#• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#• A mensagem "Reprovado", se a média for menor do que sete;
#• A mensagem "Aprovado com Distinção", se a média for igual a dez.

a = int(input("Digite a sua nota 1: "))
b = int(input("Digite a sua nota 2: "))
media = (a + b)/2
if media == 10: print("Aprovado com Distinção :) ")
elif media >=7 and media < 10: print("Aprovado! ")
else: print("Reprovado! ")