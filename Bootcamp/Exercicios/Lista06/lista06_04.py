'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sexta Lista de Exercicios - Funções
Abril/2022.
'''

# Exercício 4) Embaralha palavras: Construa uma função que receba uma string como parâmetro e 
# devolva outra string com os carateres embaralhados.

def Embaralha_String (string_entrada: str) -> str:
    '''
    Esse programa embaralha a string de entrada.

        Args:
        string_entrada: str
        Output:
        string_embaralhada: str    
    
    '''

    from random import shuffle

    string_lista =[]
    string_entrada = string_entrada.lower()

    for caracter in string_entrada:
        string_lista.append(caracter)
    
    shuffle(string_lista)
    string_embaralhada = "".join(string_lista)

    return string_embaralhada

print(Embaralha_String('Python'))