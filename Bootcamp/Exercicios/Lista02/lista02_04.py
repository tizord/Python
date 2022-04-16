'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 4) Faça um programa que receba a temperatura média por mês do ano e armazena-as 
# em uma lista. Depois calcule e média de temperatura anual e retorne os meses cuja 
# temperatura está acima da média, no formato: 1 - Janeiro.

temperatura = []
meses = ["Janeiro", "Favereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for _ in range(0, 12):
    temperatura.append(float(input(f"Insira a temperatura do mês {meses[_]}: ")))

temperatura_media = sum(temperatura)/len(temperatura)

print(f"A temperatura média é {temperatura_media:.2f} °C\n")

for _ in range(0,12):

    if temperatura[_] > temperatura_media:
        print(f"O mês {_+1} - {meses[_]} tem temperatura acima da média: {temperatura[_]} °C")

