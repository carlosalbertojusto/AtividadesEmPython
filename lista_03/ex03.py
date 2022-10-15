#. Faça um programa que leia e valide as seguintes informações:
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 1-feminino ou 2-masculino;
#e. Estado Civil: 1-solteiro, 2-casado, 3-viuvo, 4-divorciado;
#Carlos Alberto

idade = 0
salario = 0
sexo = 0
estCivil = 0

idade=int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: "))
sexo = int(input("Digite seu sexo, 1. Feminino ou 2. Masculino: "))
estCivil = int(input(
    "Digite seu estado civil 1. Solteiro, 2. Casado, 3. Viúvo ou 4. Divorciado: "
    ))

while (idade < 0 or idade > 150 ):
    print("Idade inválida!")
    idade=int(input("Digite sua idade novamente: "))

while salario<0:
    print("Salário inválido!")
    salario=float(input("Digite seu sálario novamente: "))

while sexo < 0 or sexo > 2:
    print("Sexo inválido!")
    sexo = int(input("Digite seu sexo novamente, 1. Feminino ou 2. Masculino: "))

while estCivil < 0 or estCivil > 4:
    print("Estado cívil inválido")
    estCivil = int(input(
    "Digite seu estado civil novamente 1. Solteiro, 2. Casado, 3. Viúvo ou 4. Divorciado: "
    ))

print("Idade: ",idade,"Salário: %.2f "%salario,"Sexo: ",sexo,"Estado Cívil: ",estCivil)