#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
# Carlos Alberto

inicio = 0
fim = 0

inicio = int(input("Digite o início com um valor inteiro: "))
fim = int(input("Digite o fim com um valor inteiro: "))

while inicio<fim-1:
    inicio=inicio+1
    print(inicio)        