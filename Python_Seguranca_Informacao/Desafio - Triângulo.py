# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo,
# calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem:
#
# Perimetro = XX.X
#
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
#
# Area = XX.X
#
# Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2
#
# Entrada
# A entrada contém três valores reais.
#
# Saída
# O resultado deve ser apresentado com uma casa decimal.


lado = [float(x) for x in input().split()]

if lado[0] + lado[1] > lado[2] and lado[0] + lado[2] > lado[1] and lado[1] + lado[2] > lado[0]:
  print(f"Perimetro = {sum(lado):.1f}")
else:
  print(f"Area = {((lado[0] + lado[1]) *  lado[2]) / 2:.1f}")