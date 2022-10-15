#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
# download do arquivo usando este link (em minutos)

# Carlos Alberto
arq = float(input("Digite o tamanho do arquivo para o download em MB: "))
velD = float(input("Digite a velocidade do link em MBps: "))

print('O tempo para o fim do download é: %.2f' % ( arq / (velD/8) /3600), 'horas')
