#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
#comprar, sabendo que a decisão é sempre pelo mais barato.


a = int(input("Digite o valor do produto: "))
b = int(input("Digite outro valor do produto: "))
c = int(input("Digite o último valor do produto: "))
maior = a

if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

print("O produto com menor valor é:  ",menor)
