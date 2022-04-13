import random
import string

tamanho = int(input('Digite o tamanho de senha que deseja: '))  #em boas práticas de segurança da informação é usado quando a sneha um numero apartir
# de 16 caracteres

chars = string.ascii_letters + string.digits + '!@#$%¨&*()_=+,.:;/?' #armazena todas as letras maiusculas e minusculas, numeros e caracteres especiais
# recebera a estrutura de senha que sera gerada
#metodo ascii_letters () utilizara letras maiusculas e minusculas
#metodo ascii_uppercase() Utilizara apenas letras maisuculas
#metodo ascii_lowercase utilizara apenas letras minusculas

#print('chars: ', chars)

rnd = random.SystemRandom() #Instancio a classe os. urandom - biblioteca Random Classe urandom gera numero aleatório apartir do sistema operacional

print(''.join(rnd.choice(chars) for i in range(tamanho))) # o comando rnd.choice retorna uma lista com os
#caracteres randomicos, cada caracter randomico gerado na variavel char, a cara loop do for, pega um caracter aleatório gerado
