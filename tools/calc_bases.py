div = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'

print('''
1 - Conversor de bases
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
2 - Calculadora de bases
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')

esc = int(input('Escolha: '))

print(div)

if esc == 1:

    def mostra_bases():
        print('Numero: {} em binario = {}'.format(num, bin(num)))
        print('Numero: {} em decimal = {}'.format(num, int(num)))
        print('Numero: {} em octal = {}'.format(num, oct(num)))
        print('Numero: {} em hex = {}'.format(num, hex(num)))

    print(div)

    print('''Coversor de bases!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
De base:
1: Binario
2: Decimal
3: Octal
4: Hex''')

    base_input = int(input('--> '))

    print(div)

    if base_input == 1:
        num = int(input("Numero para conversão (binario): "), 2)
        mostra_bases()
        print(div)
    elif base_input == 2:
        num = int(input("Numero para conversão (decimal): "))
        mostra_bases()
        print(div)
    elif base_input == 3:
        num = int(input("Numero para converção (octal): "), 8)
        mostra_bases()
        print(div)
    elif base_input == 4:
        num = int(input("Numero para converção (hex): "), 16)
        mostra_bases()
        print(div)
    else:
        print("Base Invalida!")
elif esc == 2:

    def mostrar_opera():
        print('''Escolha a operação:
1 - soma
2 - subtração
3 - multiplicação
4 - divisão''')

    print('''
Calculadora de bases!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha a base:
1: Binario
2: Decimal
3: Octal
4: Hex''')

    esc = int(input('Escolha: '))

    if esc == 1:

        mostrar_opera()

        esc = int(input('Escolha: '))

        num1 = int(input("Numero 1 (binario): "), 2)
        num2 = int(input("Numero 2 (binario): "), 2)

        if esc == 1:
            soma = num1+num2
            print('Soma =', bin(soma))
        elif esc == 2:
            subt = num1-num2
            print('Subtração =', bin(subt))
        elif esc == 3:
            mult = num1*num2
            print('Multiplicação =', bin(mult))
        elif esc == 4:
            divs = num1/num2
            divs = int(divs)
            print('Divisão =', bin(divs))

    elif esc == 2:

        mostrar_opera()

        esc = int(input('Escolha: '))

        num1 = int(input("Numero 1 (decimal): "))
        num2 = int(input("Numero 2 (decimal): "))

        if esc == 1:
            soma = num1+num2
            print('Soma =', soma)
        elif esc == 2:
            subt = num1-num2
            print('Subtração =', subt)
        elif esc == 3:
            mult = num1*num2
            print('Multiplicação =', mult)
        elif esc == 4:
            divs = num1/num2
            divs = int(divs)
            print('Divisão =', divs)

    elif esc == 3:

        mostrar_opera()

        esc = int(input('Escolha: '))

        num1 = int(input("Numero 1 (octal): "), 8)
        num2 = int(input("Numero 2 (octal): "), 8)

        if esc == 1:
            soma = num1+num2
            print('Soma =', oct(soma))
        elif esc == 2:
            subt = num1-num2
            print('Subtração =', oct(subt))
        elif esc == 3:
            mult = num1*num2
            print('Multiplicação =', oct(mult))
        elif esc == 4:
            divs = num1/num2
            divs = int(divs)
            print('Divisão =', oct(divs))
    elif esc == 4:

        mostrar_opera()

        esc = int(input('Escolha: '))

        num1 = int(input("Numero 1 (hex): "), 16)
        num2 = int(input("Numero 2 (hex): "), 16)

        if esc == 1:
            soma = num1+num2
            print('Soma =', hex(soma))
        elif esc == 2:
            subt = num1-num2
            print('Subtração =', hex(subt))
        elif esc == 3:
            mult = num1*num2
            print('Multiplicação =', hex(mult))
        elif esc == 4:
            divs = num1/num2
            divs = int(divs)
            print('Divisão =', hex(divs))
    else:
        print('Escolha invalida!')


# code-by-porquezin!
