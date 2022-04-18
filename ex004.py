#Alistamento militar

import datetime

print('+-------------------------------------+')
print('|          ALISTAMENTO 2022           |')
print('+-------------------------------------+')

nome = input('Digite seu nome: ').upper()
ano_nascimento = int(input('Digite seu ano de nascimento: '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano_atual = date.year


alistamento = (ano_atual - ano_nascimento)

if alistamento == 18:
    print('{}, você tem 18 anos e está na hora de se alistar'.format(nome))

elif alistamento > 18:
    passou = alistamento - 18
    print('{}, já  se passaram {} anos do alistamento'.format(nome,passou))
else:
    faltam = 18 - alistamento
    print('{}, faltam {} anos para o alistamento. Não se esqueça!'.format(nome,faltam))
