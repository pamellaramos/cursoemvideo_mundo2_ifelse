#Analisando triangulos (refazer o 35)

a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))

if ((b-c)%2)<a<(b+c):
    if ((a-c)%2)<b<(a+c):
        if ((a-b)%2)<c<(a+b):

            if a == b and a == c and b == c:
                print('É um triângulo EQUILÁTERO')
            elif a == b or a == c and b != c:
                print('É um triângulo ISÓCELES')
            else:
                print('É um triângulo ESCALENO')
        else:
            print('Não é um triângulo')
    else:
        print('Não é um triângulo')
else:
    print('Não é um triângulo')

