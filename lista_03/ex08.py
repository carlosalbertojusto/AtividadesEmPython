# Faça um programa que leia 5 números e informe a soma e a média dos números.
# Carlos Alberto

num = []
for i in range(5):
    n=int(input("Digite um número: "))
    num.append(n)

print("Soma: ",sum(num),"Média: ",sum(num)/5)