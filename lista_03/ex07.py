# Faça um programa que leia 5 números e informe o maior número
# Carlos Alberto
num = []
for i in range(5):
    n=int(input("Digite um número: "))
    num.append(n)
print(max(num))