#estruturas de repetição

#for: Uma vez que n é menor do que 10 (condição), o comando print é executado.
#Essa condição é adicionada com o comando range.
#A variável n é incrementada em 1 (incremento padrão) e é testado se o valor de n ainda é menor do que 10.
#O processo se repete até que o valor de n fique maior ou igual a 10.
for n in range(10):
    print(n)

#for determinando o valor inicial
for n in range(5, 16):
    print(n)

#decremento no contador, dentro do comando range.
for n in range(10, 0, -1):
    print(n)


#While
#diferente da estrutura For, na estrutura While temos de inicializar a variável antes do início do laço (x=1;) 
#e, também, realizar o incremento dentro do bloco de repetição (x=x+1;)
x=1;
while x<=15:
    print(x);
    x=x+1

#exemplo
qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor: "))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ", media)