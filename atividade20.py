# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

from random import randint

numero = randint(0,5)
print('')
print('Vou sortear um número de 0 a 5.')
print('')
usuario = int(input('Adivinhe o número: '))

if usuario == numero:
    print("Voçê VENCEU!!!")
else:
    print('Voçê PERDEU AAKAKAAKAKAK TENTE DE NOVO;)')
