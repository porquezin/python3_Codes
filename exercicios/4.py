num = input('Digite um numero inteiro -> ')

try:
    num = int(num)
    if num % 2 == 0:
        print('Numero par!')
    else:
        print('Numero impar!')
except:
    print('ERROR!')