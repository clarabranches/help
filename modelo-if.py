#modelo if
idade = int(input("Digite a sua idade: "))
if idade > 18:
    print("Você já é maior de idade")


#modelo if com else
idade = int(input("Digite a sua idade: "))
if idade > 18:
    print("Você já é maior de idade")
else:
    print("Você ainda é menor de idade")


#modelo if com elif e else
idade = int(input("Digite a sua idade: "))
if idade > 18:
    print("Você já é maior de idade")
elif idade > 12:
    print("Você ainda é adolescente")
else:
    print("Você é uma criança")