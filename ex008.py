#índice de massa

print('+-------------------------------------+')
print('|                IMC                  |')
print('+-------------------------------------+')

peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))

imc = (peso / (altura * altura))

if imc < 18.5:
    print('IMC = {:.1f} - \033[0;36mAbaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC = {:.1f} - \033[0;34mPeso Ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC = {:.1f} - \033[0;32mSobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('IMC = {:.1f} - \033[0;33mObesidade'.format(imc))
else:
    print('IMC = {:.1f} - \033[0;31mObesidade Mórbida'.format(imc))
