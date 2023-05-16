# Faça um programa que leia um número inteiro e mostre na tela sua tabuada

numero_1 = int(input('Digite um valor: '))
print('-='*20)
for c in range(1, 11):
    print('{} x {} = {}'.format(numero_1, c, numero_1*c))
print('-='*20)
