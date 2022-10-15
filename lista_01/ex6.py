#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# Carlos Alberto

salarioH = float(input("Digite o valor das suas horas trabalhadas: "))
horasT = int(input("Digite a quantidade de horas trabalhadas: "))

salario_mes = salarioH * horasT

print("O valor recebido de salário por mês é: ", salario_mes)