# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa
# que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
# salário atual:


salario = float(input("Digite seu salário: "))

salarioBaixo = salario * 0.20
baixo = salario * 1.20
salarioMedio = salario * 0.15
medio = salario * 1.15
salarioAlto = salario * 0.10
alto = salario * 1.10
salarioAltissimo = salario * 0.05
altissimo = salario * 1.05

print("Salário antes do reajuste: %.2f " %(salario))

if salario <= 280:
    print("O percentual de aumento: 20% O valor do aumento: " ,salarioBaixo, "O salário reajustado: ",baixo )
if salario > 280 and salario <= 700:
    print("O percentual de aumento: 15%  O valor do aumento: ",salarioMedio, "O salário reajustado: ",medio)
if salario > 700 and salario < 1500:
    print("O percentual de aumento: 10% / O valor do aumento: ",salarioAlto, "O salário reajustado: ",alto)
if salario >= 1500:
    print("O percentual de aumento: 5% / O valor do aumento: ",salarioAltissimo, "O salário reajustado: ",altissimo)
