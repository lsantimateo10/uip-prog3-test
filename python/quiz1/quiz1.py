vali = 10
f = 0
sum = 0

while vali < 5000:

    if vali%2 == 0:

        f += vali

        sum = f-1100

    vali += 1

print('La suma de los pares es igual a %i' % sum)