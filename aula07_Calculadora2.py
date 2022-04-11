class Calculadora:

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def substracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora_var = Calculadora() # Esta Instanceando a Classe, basicamente é inicializar os parametros/ variaveis que serão utilizados na classe

# print('Teste Classes Soma: ',Calculadora.soma(10,2))

print('Calc: ', Calculadora.soma(0,10,2))

print(calculadora_var.soma(10,2))
print(calculadora_var.substracao(5,3))
print(calculadora_var.multiplicacao(100,2))
print(calculadora_var.divisao(10,5))