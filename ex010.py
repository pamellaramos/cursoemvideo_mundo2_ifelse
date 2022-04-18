#Jokepô
import random

lista = ['PAPEL', 'TESOURA', 'PEDRA']

jogador = input('Digite PAPEL, TESOURA ou PEDRA: ').upper()
escolha = random.choice(lista)
print('A máquina escolheu {}' .format(escolha))

if jogador == 'PAPEL':
    if escolha == 'PAPEL':
        print('Empate')
    if escolha == 'TESOURA' or escolha == 'PEDRA':
        print('Você perdeu!')

elif jogador == 'TESOURA':
   if escolha == 'PAPEL':
      print('Você ganhou!')
   if escolha == 'TESOURA':
      print('Empate')
   if escolha == 'PEDRA':
      print('Você perdeu!')
else:
   print('Você ganhou! ')
