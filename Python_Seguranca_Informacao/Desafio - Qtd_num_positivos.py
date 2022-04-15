counter = 0
for x in range(6):
    number = float(input('digite o numero: '))
    if number > 0:
        counter += 1

print("{} valores positivos".format(counter))