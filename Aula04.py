a = int(input("Primeiro nota do Bimestre: "))
while a > 10 or a < 0:
    a = int(input("Valor Inválido, Digite a Nota do Primeiro Bimestre: "))
b = int(input("Segunda nota do Bimestre: "))
while b > 10 or b < 0:
    b = int(input("Valor Inválido, Digite a Nota do Segunda Bimestre: "))
c = int(input("Terceira nota do Bimestre: "))
while c > 10 or c < 0:
    c = int(input("Valor Inválido, Digite a Nota do Terceiro Bimestre: "))
d = int(input("Quarta nota do Bimestre: "))
while d > 10 or d < 0:
    d = int(input("Valor Inválido, Digite a Nota do Quarto Bimestre: "))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("media: {}".format(media))
else:
    print("Foi informado alguma nota errada")


# # Exibe os numeros primos até o numero digitado
# a = int(input('Entre com o número: '))
# for num in range (a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#        # print(x, resto)
#         if resto ==0 :
#             div +=1
#     if div == 2:
#         print(num)


# Verifica se um numero é primo
# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1,a +1):
#     resto = a % x
#     print(x, resto)
#     if resto ==0 :
#         div +=1
#
# if div == 2:
#     print("número {} é primo". format(a))
# else:
#     print("número {} não é primo". format(a))