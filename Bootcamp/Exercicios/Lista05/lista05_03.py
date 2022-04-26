'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''

# Exercício 3) Um determinado zoológico cobra a entrada com base na idade do visitante. 
# Os visitantes com 2 anos de idade ou menos não pagam para entrar. 
# Crianças entre 3 e 12 anos custa R$14,00. 
# Idosos com 65 anos ou mais custam R$18,00. 
# A entrada para todos os outros visitantes é de R$23,00. 
# Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, 
# com uma idade inserida em cada linha. O usuário digitará uma linha em branco para indicam que não há 
# mais visitantes no grupo.

grupo_visitante = []
ate_2_anos = 0
entre_3_e_12_anos = 0
idosos_65_anos_ou_mais = 0
entre_13_e_65_anos = 0

idade_visitante = input("Insira a idade do visitante: ")

if idade_visitante == ' ':
    print("Você deu o comando de parada")
else:
    grupo_visitante.append(idade_visitante)

while idade_visitante != ' ':
    idade_visitante = input("Insira a idade do visitante: ")
    if idade_visitante != ' ':
        grupo_visitante.append(idade_visitante)

grupo_visitante = list(map(int, grupo_visitante))

for visitante in grupo_visitante:
    if visitante <= 2:
        ate_2_anos += 1
    if visitante >= 3 and visitante <= 12:
        entre_3_e_12_anos += 1
    if visitante >= 13 and visitante < 65:
        entre_13_e_65_anos += 1
    if visitante >= 65:
        idosos_65_anos_ou_mais += 1

preco_total = float(
    ate_2_anos * 0 +
    entre_3_e_12_anos * 14 +
    idosos_65_anos_ou_mais * 18 +
    entre_13_e_65_anos * 23
)

print(f'O custo de admissão do grupo composto por:\n - {ate_2_anos} pessoas até 2 anos (gratuito)\n - {entre_3_e_12_anos} crianças entre 3 e 12 anos (R$ 14,00/pessoa)\n - {idosos_65_anos_ou_mais} idosos com 65 anos ou mais (R$ 18,00/pessoa)\n - {entre_13_e_65_anos} demais visitantes (R$ 23,00/pessoa) é: \n R$ {preco_total:.2f}')