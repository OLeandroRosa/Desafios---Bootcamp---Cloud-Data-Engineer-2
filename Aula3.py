a = int(input("Nota Primeiro Bimestre: "))
b = int(input("Nota Segundo Bimestre: "))
c = int(input("Nota Terceiro Bimestre: "))
d = int(input("Nota Quarto Bimestre: "))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("media: {}".format(media))
else:
    print("Foi informado alguma nota errada")











# a = int(input('primeiro valor: '))
# b = int(input('segundo valor: '))
# c = int(input('terceiro valor: '))
# if a > b and a > c:
#     print ('o Maior número é {}'. format(a))
# elif b > a and b > c:
#     print ('O maior número é {}'. format(b))
# else:
#     print ('O maior número é {}'.format(c))
# print('Final do programa - Aula 03')


# a  = int(input("Entre com o primeiro valor: "))
# b = int(input("Entre com o segundo valor: "))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Número é par')
# else:
#     print ('Número é impar')

