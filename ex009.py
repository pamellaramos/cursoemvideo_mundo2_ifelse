#Gerenciador de pagamentos

print('+-------------------------------------+')
print('|              VENDA                  |')
print('+-------------------------------------+')

valor_produto = float(input('Valor: R$'))

for i in range(10):
        print('+---------------------------------------+')
        print('|       Condições de pagamento          |')
        print('+---------------------------------------+')
        print('|     [ 1 ] - À vista dinheiro/cheque   |')
        print('|     [ 2 ] - À vista cartão            |')
        print('|     [ 3 ] - 2x no cartão              |')
        print('|     [ 4 ] - 3x ou mais no cartão      |')
        print('|     [ 5 ] - Sair                      |')
        print('+---------------------------------------+')
        opcao = int(input("Qual operação voce deseja realizar? "))

        if opcao == 1:
            valor = valor_produto * 0.9
            print('Total = R${:.2f}'.format(valor))
            print('Venda realizada com 10% de desconto')
            print('\n')
        elif opcao == 2:
            valor = valor_produto * 0.95
            print('Total = R${:.2f}'.format(valor))
            print('Venda realizada com 5% de desconto')
            print('\n')
        elif opcao == 3:
            print('Total = R${:.2f}'.format(valor))
            print('Valor da parcela = R${:.2f}'.format((valor/2)))
            print('Venda realizada sem juros')
            print('\n')
        elif opcao == 4:
            valor = valor_produto * 1.2
            print('Total = R${:.2f}'.format(valor))
            n = int(input('Informe o número de parcelas: '))
            print('Valor da parcela = R${:.2f}'.format((valor / n)))
            print('Venda realizada com 20% de juros')
            print('\n')
        elif opcao == 5:
            print('\n')
            print('Fim')
            break



