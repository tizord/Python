'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quarta Lista de Exercicios - Condicionais
Abril/2022.
'''

# Exercício 3) Escreva um programa que leia um valor de nível sonoro do usuário em decibéis.
# Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho.
# Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais
# barulhos o valor digitado está. Seu programa deve informar também quando o valor for menor
# que o ruído mínimo da tabela e maior que ruído máximo.

nivel_sonoro_db = dict(zip([130, 106, 70, 40], ['Britadeira', 'Cortador de Grama', 'Despertador', 'Cômodo em silêncio']))

procura_nivel_db = int(input('Insira o nível em dB que desejas procurar: '))

lista_valores_db = list(nivel_sonoro_db.keys())

for chave in nivel_sonoro_db.keys():
    if procura_nivel_db in nivel_sonoro_db:
        print(f'O valor {procura_nivel_db} dB corresponde ao barulho de {nivel_sonoro_db[procura_nivel_db]}')
        break

    elif procura_nivel_db > max(lista_valores_db):
        print(f'O valor {procura_nivel_db} dB é maior do que o maior valor da lista: {max(lista_valores_db)} dB - {nivel_sonoro_db[max(lista_valores_db)]}')
        break

    elif procura_nivel_db < min(lista_valores_db):
        print(f'O valor {procura_nivel_db} dB é menor do que o menor valor da lista: {min(lista_valores_db)} dB - {nivel_sonoro_db[min(lista_valores_db)]}')
        break

    elif procura_nivel_db > min(lista_valores_db) and procura_nivel_db < lista_valores_db[2]:
        print(f'O valor de {procura_nivel_db} dB está entre {nivel_sonoro_db[min(lista_valores_db)]} e {nivel_sonoro_db[lista_valores_db[2]]} ')
        break

    elif procura_nivel_db > lista_valores_db[2] and procura_nivel_db < lista_valores_db[1]:
        print(f'O valor de {procura_nivel_db} dB está entre {nivel_sonoro_db[lista_valores_db[2]]} e {nivel_sonoro_db[lista_valores_db[1]]} ')
        break

    elif procura_nivel_db > lista_valores_db[1] and procura_nivel_db < lista_valores_db[0]:
        print(f'O valor de {procura_nivel_db} dB está entre {nivel_sonoro_db[lista_valores_db[1]]} e {nivel_sonoro_db[lista_valores_db[0]]} ')
        break   