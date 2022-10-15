#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Carlos Alberto
nota = 0
nota = int(input("Digite sua nota: "))
while nota < 0 or nota > 10:
    print("Nota inválida!!")
    nota = int(input("Digite uma nota válida: "))