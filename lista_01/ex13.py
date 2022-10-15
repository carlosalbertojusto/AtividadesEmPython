#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
#metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Carlos Alberto

area = float(input("Digite o valor da área a ser pintada em m²: "))
qtdTinta = area * (1/3)
latasTinta = qtdTinta / 18
print('Quantidade de tinta: %.2f' %(latasTinta) + 'O Preço total: %.2f' %(latasTinta * 80))