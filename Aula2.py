a =  int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

soma =  a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a %b

print (soma)
print ('soma: ' + str(soma))
print ('Soma: {soma}. \nSubtração: {subtracao}.'
       '\nMultiplicação: {multiplicacao}'
       '\nDivisão: {divisao}'
       '\nResto: {resto}' .format(soma= soma,
                                   subtracao = subtracao,
                                   multiplicacao = multiplicacao,
                                   divisao = divisao,
                                   resto = resto))



'''print(subtracao)
print(multiplicacao)
print(divisao)
print (resto)'''

#print("soma", soma)

print("Fim do Programa - Aula 02 - Operadores aritméticos")