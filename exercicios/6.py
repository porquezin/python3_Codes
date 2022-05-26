nome = input('Nome -> ')

nome = len(nome)

if nome <= 4:
    print('Curto!')
elif nome > 4 and nome <= 6:
    print('Medio!')
else:
    print('Grande!')