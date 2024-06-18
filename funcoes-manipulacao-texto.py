arquivo = open("arqText.txt", "w")

arquivo.write("Curso Python \n")
arquivo.write("Aula pratica \n")
arquivo.close()

#leitura do arquivo texto

leitura = open("arqText.txt", "r")
print(leitura.read())
leitura.close()