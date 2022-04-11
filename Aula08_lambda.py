contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']

# print(contador_letras(lista_animais))
# print(soma(10,5))
# print(subtracao(70,9))


calculadora = {
    'soma': lambda a,b : a+b,
    'subtracao':lambda a,b : a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao' : lambda a,b: a / b,
}

print(type(calculadora))

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']

print('A soma é: {}'.format(soma(20,90)))
print('A Multiplicacao é: {}'.format(multiplicacao(2,80)))