conjunto  = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)


conjunto_interseccao = conjunto.intersection(conjunto2)
print('conjunto_interseccao: ',conjunto_interseccao)

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('conjunto_diferenca1, diferença entre 1 e 2: ', conjunto_diferenca1)
print('conjunto_diferenca2, diferença entre 2 e 1:', conjunto_diferenca2)

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'. format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print("conjunto_subset:", conjunto_subset)

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print("conjunto_superset:", conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('lista:', lista)
conjunto_animal = set(lista)
print('conjunto animal: ',  conjunto_animal)

listas_animal = list(conjunto_animal)
print('lista animal: ', listas_animal)


# conjunto.add(5)
# conjunto.discard(2)
# print (type(conjunto))