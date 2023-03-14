import sys
import datetime
import calendar
from math import pi

'''#primeiro exercicio - pegar a versão do sistema
print('System Version')
print(sys.version)
print('System Info')
print(sys.version_info)'''

'''#segundo exercicio - pegar a data e hora atuais
now = datetime.datetime.now()
print('Current data and time:')
print(now.strftime("%Y-%B-%d  %H:%M:%S"))'''

'''#terceiro exercicio - achar a area de uma esfera atraves da entrada do raio pelo usuario
raio = float(input('entre com o raio da esfera:'))
area_da_esfera = pi * raio**2
print('A area da esfera é ' + str(area_da_esfera))'''

'''#quarto exercicio - pegar o nome e sobrenome do usuario e mostrar ele invertido
usuario_nome = list(input('enter your first name and your second name:').split())
print(usuario_nome)
usuario_nome.reverse()
inverso = ' '.join(usuario_nome)
print(inverso)'''

'''#quinto exercicio - entrar com numeros separados por virgula e mostrar uma lista e uma tupla com os respectivos valores
lista = input("Entre com numeros separados por virgula:")
nova_lista = lista.split(",")
tupla = tuple(nova_lista)
print('Lista: ', nova_lista)
print('Tupla: ', tupla)'''

'''
color_list = ["Red","Green","White" ,"Black"]
print(f'{color_list[0]}, {color_list[-1]}')'''

'''#setimo exercicio - receber um ano e um mes do usuario e mostrar todo o mes do calendario
year = int(input('entre com o ano:'))
month = int(input('entre com o mes:'))
print(calendar.month(year, month))'''


