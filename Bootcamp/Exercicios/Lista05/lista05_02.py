'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''
temperatura_celcius = list(range(0,101,10))
temperatura_farenheit = []

for temperatura in temperatura_celcius:
    temp_far = ((temperatura * (9 / 5)) + 32)
    temperatura_farenheit.append(temp_far)


print(24*"-")
print('|   CONVERSÃO °C -> °F |')
print(24*"-")
print('| TEMP. °C |  TEMP. °F |')
print(24*"-")
for _ in range(0,11):
    print(f'|  {str(temperatura_celcius[_]).zfill(3)} °C  |  {str(temperatura_farenheit[_]).zfill(5)} °F |')

print(24*'-')