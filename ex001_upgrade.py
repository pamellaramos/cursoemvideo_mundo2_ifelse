#aprovação de emprestimo bancário


print('+-------------------------------------+')
print('|       INSIRA AS INFORMAÇÕES         |')
print('+-------------------------------------+')
print('\n')

valor_casa = float(input('Valor do imóvel: R$'))
salario = float(input('Renda mensal: R$'))
tempo = int(input('Tempo de financiamento em meses: '))
i = float(input('Taxa de juros mensal em % '))
i_f = i /100
cf = i_f / (1 - (1 / (1 + i_f) ** tempo))

prestacao = valor_casa * cf
salario_porcentagem = salario * 0.3

print('\n')
print('+--------------------------------------+')
print('Valor do Financiamento: R${:.2f}'.format(valor_casa))
print('Salário: R${:.2f}'.format(salario))
print('Tempo: {} meses'.format(tempo))
print('Valor da prestação: R${:.2f}'.format(prestacao))
print('30% salário: R${:.2f} '.format(salario_porcentagem))
print('+--------------------------------------+')
print('\n')

if salario_porcentagem >= prestacao:
    print('Seu crédito foi aprovado')
else:
    print('Infelizmente seu crédito não foi aprovado!')


