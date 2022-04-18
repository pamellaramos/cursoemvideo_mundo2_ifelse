#Média
print('+-------------------------------------+')
print('|          MÉDIA 1ºBIMESTRE           |')
print('+-------------------------------------+')

nome = input('Digite seu nome: ').upper()
print('+-------------------------------------+')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('{}, sua média é {:.1f}. Status: \033[0;31mREPROVADO'.format(nome,media))
elif 5.0 < media < 6.9:
    print('{}, sua média é {:.1f}. Status: \033[0;32mRECUPERAÇÃO'.format(nome, media))
else:
    print('{}, sua média é {:.1f}. Status: \033[0;34mAPROVADO'.format(nome, media))