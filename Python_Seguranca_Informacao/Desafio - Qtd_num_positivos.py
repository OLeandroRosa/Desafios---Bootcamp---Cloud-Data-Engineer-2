# Desafio
# Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos.
# Em seguida, apresente a quantidade de valores positivos digitados.
#
# Entrada
# Você receberá seis valores, negativos e/ou positivos.
#
# Saída
# Exiba uma mensagem dizendo quantos valores positivos foram lidos.
# assim como é exibido abaixo no exemplo de saída. Não se esqueça de incluir na mensagem de
# saída o sufixo " valores positivos"

counter = 0
for x in range(6):
    number = float(input('digite o numero: '))
    if number > 0:
        counter += 1

print("{} valores positivos".format(counter))