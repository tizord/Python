'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sexta Lista de Exercicios - Funções
Abril/2022.
'''

# Exercício 1) Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 
# para cada 140 metros percorridos. Escreva uma função que receba a distância percorrida (em quilômetros) 
# como único parâmetro e retorna a tarifa total como único resultado. Escreva um programa que demonstre o 
# uso da sua função.

def Calcula_Tarifa(quilometragem: float) -> float:
    '''
    Função que calcula o a tarifa em função da distância (km):
        Arg:
        quilometragem (float) - Corresponde a distância em km
        Output:
        preço (float) - Corresponde ao preço da corrida

        o Preço é obtido através da função:
        4 + 0,25 * quilometragem * (140/1000)
        4 - Valor fixo
        140/1000 - Converte  
    '''

    preco = 4 + 0.25 * (quilometragem // 0.140)

    return preco

print(f"A corrida cuja distância é 1 km custará: R$ {Calcula_Tarifa(1)}")

