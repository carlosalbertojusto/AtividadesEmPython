#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar 0-matutino ou 1-Vespertino ou 2-Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
#conforme o caso

turno = int(input("Digite o seu turno: 0. Matutino, 1. Vespertino ou 2. Noturno "))

if turno == 0: print("Bom Dia!")
elif turno == 1: print("Boa Tarde!")
elif turno == 2: print("Boa noite!")
else: print("Valor Inválido!")