
#Faça um programa que informe a população dois paises, calcule e escreva o número de anos necessários para que a população do 
#país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#Carlos Alberto

popA = 0
popB = 0
anos = 0

popA = int(input("Digite a população do país A: "))
popB = int(input("Digite a população do país B: "))
while popA <= popB:
    popA = popA * 0.03
    popB = popB * 0.015
    anos += 1

print("O crescimento da população do país A demorou ",anos," anos para atingir a população do país B.")