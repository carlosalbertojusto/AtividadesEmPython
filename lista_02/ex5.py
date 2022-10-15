# Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite o último valor: "))


if a > b and a > c: print("O primeiro número é o maior: ",a)
elif b > a and b > c: print("O segundo número é o maior: ",b)
else: print("O terceiro número é o maior: ",c)