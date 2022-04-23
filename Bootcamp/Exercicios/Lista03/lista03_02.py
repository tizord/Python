'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

#Exercício 2) Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o 
#nome completo do estado.

siglas_estados = {'AC': "Acre", 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia', 'CE': 'Ceará', 'ES': 'Espírito Santo', 'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins', 'DF': 'Distrito Federal'}

procurar_sigla = input('Digite um estado: ').upper()

if procurar_sigla not in list(siglas_estados):
    print("Essa sigla não corresponde a um estado brasileiro ou está errada \n")
else:
    print(f"O nome completo do estado é {procurar_sigla} - {siglas_estados[procurar_sigla]}")