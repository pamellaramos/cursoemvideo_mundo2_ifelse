nome = str(input('Qual é o seu nome? ')).upper()

if nome == 'PAMELLA':
    print('Que nome bonito!')
elif nome =='PEDRO' or nome =='MARIA' or nome == 'PAULO':
    print('Seu nome é bem comum no Brasil')
elif nome in ('ANA, CLAUDIA, JESSICA, JULIANA'):
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(('Tenha um bom dia {}'.format(nome)))
