def capi():
    numero = input("Num: ");
    numeroInvertido = int(numero[::-1]);
    if int(numero) == int(numeroInvertido):
        print('É capicua')
    else:
        print('Não é capicua')

capi()