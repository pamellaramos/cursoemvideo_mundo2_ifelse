#Classificando atletas

import datetime

print('+-------------------------------------+')
print('|          MMA - 2022                 |')
print('+-------------------------------------+')
print('+-------------------------------------+')
print('|            CATEGORIAS               |')
print('+-------------------------------------+')
print('Mirim')
print('Infantil')
print('Júnior')
print('Senior')
print('Master')

print('+-------------------------------------+')
print('\n')

nome = input('Digite seu nome: ').upper()
ano_nascimento = int(input('Digite seu ano de nascimento: '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano_atual = date.year


idade = (ano_atual - ano_nascimento)

if idade <= 9:
    print('{}, sua categoria é \033[0;31mMirim'.format(nome))
elif 9 < idade <= 14:
    print('{}, sua categoria é \033[0;32mnfantil'.format(nome))
elif 14 < idade <=19:
    print('{}, sua categoria é \033[0;33mJúnior'.format(nome))
elif 19 < idade < 20:
    print('{}, sua categoria é \033[0;34mSenior'.format(nome))
else:
    print('{}, sua categoria é \033[0;35mMaster'.format(nome))