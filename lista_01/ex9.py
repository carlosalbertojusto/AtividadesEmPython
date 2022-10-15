#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.

# Carlos Alberto

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

prod = ((2*num1) * (num2/2))
soma = ((3*num1) + num3)
cubo = num3 ** 3

print("O produto é: " + str(prod)
      + " A Soma é: " + str(soma)
      + " O valor ao cubo é: " + str(cubo)
      )
