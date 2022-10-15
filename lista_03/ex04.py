#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual 
#de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
#de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do 
#país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#Carlos Alberto

popA = 80000
popB = 200000
anos = 0

while popA <= popB:
    popA = popA * 0.03
    popB = popB * 0.015
    anos += 1

print("O crescimento da população do país A demorou ",anos," anos para atingir a população do país B.")