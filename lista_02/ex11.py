# Faça um Programa que peça os 3 lados de um triângulo.


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o último valor: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Não pode ser um triângulo!!")
elif (a == b) and (a == c):
    print("Equilátero")
elif (a == b) or ( a == c) or (b == c):
    print("Isósceles")
else: print("Escaleno")