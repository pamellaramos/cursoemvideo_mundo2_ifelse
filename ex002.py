#Conversor de base

print('+-------------------------------------+')
print('|            CONVERSÃO                |')
print('+-------------------------------------+')

num = int(input('Digite um número: '))

for i in range(10):

        print('+---------------------------------------+')
        print('|         BASE DE CONVERSÃO             |')
        print('+---------------------------------------+')
        print('|     [ 1 ] - Binário                   |')
        print('|     [ 2 ] - Octal                     |')
        print('|     [ 3 ] - Hexadecimal               |')
        print('|     [ 4 ] - Sair                      |')
        print('+---------------------------------------+')

        opcao = int(input("Qual operação voce deseja realizar? "))

        if opcao == 1:
                binario = bin(num)
                print('O número inteiro {} em binário é {}'.format(num, binario))
        elif opcao == 2:
                octal = oct(num)
                print('O número inteiro {} em octal é {}'.format(num, octal))
        elif opcao == 3:
                hexa = hex(num)
                print('O número inteiro {} em hexadecimal é {}'.format(num, hexa))
        else:
                print('Obrigada')
                break



