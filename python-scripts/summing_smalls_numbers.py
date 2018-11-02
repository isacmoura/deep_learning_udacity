# Somando pequenos números a um número de 1 bilhão

big = 10 ** 9

for i in range (10 ** 6):
    big += 10 ** -6

big -= 10 ** 9
print("{0:.3f}".format(big))

# O resultado não é 1
