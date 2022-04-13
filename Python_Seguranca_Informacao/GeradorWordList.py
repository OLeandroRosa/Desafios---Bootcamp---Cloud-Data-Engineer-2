import itertools

string = input('String a ser permutada: ')


resultado = itertools.permutations(string,len(string)) #recebe da itertools o metodo chamado permutations, faz a permutação das palavras dos caracteres no wordlist
#1° parametro palavra, 2° parametro quantas permutações, não pode ser maior que a quantidade de caracteres no parametro 1
# print(''.join(resultado))
# print(type(resultado))

for i in resultado:
    print(''.join(i)) #junta os caracteres