class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma (self):
        return self.valor_a + self.valor_b

    def substracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao (self):
        return self.valor_a * self.valor_b

    def divisao (self):
        return self.valor_a / self.valor_b
if __name__ == '__main__':
    calculadora = Calculadora(10, 2) # Esta Instanceando a Classe, basicamente é inicializar os parametros/ variaveis que serão utilizados na classe
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.substracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
