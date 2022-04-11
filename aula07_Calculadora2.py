class Calculadora:

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def substracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora() # Esta Instanceando a Classe, basicamente é inicializar os parametros/ variaveis que serão utilizados na classe

print(calculadora.soma(10,2))
print(calculadora.substracao(5,3))
print(calculadora.multiplicacao(100,2))
print(calculadora.divisao(10,5))