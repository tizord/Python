'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sexta Lista de Exercicios - Funções
Abril/2022.
'''

# Exercício 2) Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas 
# podem ou não formar um triângulo, retornando true em caso positivo e false em caso negativo

def Verifica_Triangulo(l1: int, l2: int, l3: int) -> bool:

    '''
    Essa função verifica se, dados 3 comprimentos de reta quaisquer, estes formam um triângulo

        Args:
            l1: int (lado 1)
            l2: int (lado 2)
            l3: int (lado 3)
        
        Output:
            bool 
    
    '''
    lados = [l1, l2, l3]
    for lado in lados:
        if lado <= 0:
            return False
        
    if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
        return False
    else:
        return True

print(f'Verificando se os segmentos 3, 4 5 formam um triângulo: Resp: {Verifica_Triangulo(3, 4, 5)}')
print(f"É possível formar um triângulo com os lados 1, 1 e 10? Resp: {Verifica_Triangulo(1,1,10)}")
print(f"É possível formar um triângulo com os lados 0, 4 e 5? Resp: {Verifica_Triangulo(0,4,5)}")