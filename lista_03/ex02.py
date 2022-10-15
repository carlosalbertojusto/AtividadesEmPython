#Faça um programa que leia um código(número) de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# Carlos Alberto
print(" Login ")
codigo = 0
codigo = int(input("Digite seu código de usúario: "))
senha = int(input("Digite sua senha: "))
while senha == codigo:
    print("Senha inválida!!")
    senha = int(input("Digite sua senha: "))