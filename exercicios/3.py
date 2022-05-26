def main(x, y, z):

    v = [x, y, z]

    if v[0] > v[1] > v[2]:
        return 1
    else:
        return 0

x = input('Num1 = ')
y = input('Num2 = ')
z = input('Num3 = ')

print(main(x, y, z))