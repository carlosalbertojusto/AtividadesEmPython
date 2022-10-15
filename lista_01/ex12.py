# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Carlos Alberto

salarioH = float(input("Digite o valor da sua hora trabalhada: "))
horasT = int(input("Digite quantas horas foram trabalhadas no mês: "))
salarioMensal = salarioH * horasT
ir = salarioMensal * 0.11
inss = salarioMensal * 0.08
sindicato = salarioMensal * 0.05
descontos = ir + inss + sindicato
print('Salário Bruto: %.2f' %(salarioMensal))
print('Inss Pago: %.2f' %(inss))
print('Sindicato Pago: %.2f' %(sindicato))
print('Salário liquido: %.2f' %(salarioMensal - descontos))
