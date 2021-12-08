# salva as contas digitas no txt
with open("contas.txt", "w") as arquivo:
    x = input('digite as contas com virgula: ')
    arquivo.write(x)

# consulta as contas digitas no txt
with open("contas.txt", "r") as tf:
    lines = tf.read().split(',')
# imprime as contas digitas no txt
for line in lines:
    print(line)
