from Aula07_televisao import Televisao
from Aula07_Calculadora1 import Calculadora
from Aula08_contador_letras import contador_letras, teste

if __name__ =='__main__' :
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5,2)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras((lista))
    print('total de letras por palavra de lista: {}'.format(total_letras))
    print(teste())