# Faça um Programa que leia três números e mostre o maior e o menor deles.


a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite o último valor: "))
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

print("O menor número digitado foi ",menor)
print("O maior número digitado foi ",maior)