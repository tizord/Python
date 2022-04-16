from time import sleep
from random import choice

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "."
ROBO = "4"
SAIDA = "S"
PILHA = []
ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]
DIRECOES = [BAIXO, DIREITA, ESQUERDA, CIMA]
DIRECAO_TESTADA = []
DIRECAO_CAMINHADA = []

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]
INDICE_SAIDA = [9,18]

def print_labirinto():
    '''
    Essa funcao imprime o labirinto:

    Input:
        None

    Output:
        None
    '''

    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")

print_labirinto()


def movimento(posicao: tuple, direcao: list):

    '''
    Essa função executa o movimento do robô. Além disso, ela escreve na pilha os movimentos feitos.

    Inputs:
        posicao: posicao atual
        direcao: direcao que ele deve andar

    Outputs:
        posicao_nova: Nova posicao que o robô chegou apos andar
    '''
        
    posicao_nova = [list(posicao)[0] + direcao[0], list(posicao)[1] + direcao[1]]

    LABIRINTO[list(posicao)[0]][list(posicao)[1]] = CAMINHO_PERCORRIDO

    if not PILHA[-1] == posicao_nova:

        PILHA.append(list(posicao_nova))

    LABIRINTO[posicao_nova[0]][posicao_nova[1]] = ROBO

    return(posicao_nova)
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:

    posicao_pretendida = [list(posicao)[0] + direcao[0], list(posicao)[1] + direcao[1]]

    if (
        LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == PAREDE or
         LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == CAMINHO_PERCORRIDO):
        for dir in DIRECOES:
            posicao_pretendida = [list(posicao)[0] + dir[0], list(posicao)[1] + dir[1]]
            if LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == CAMINHO_LIVRE:
                return False

        for dir in DIRECOES:
            posicao_pretendida = [list(posicao)[0] + dir[0], list(posicao)[1] + dir[1]]
            if posicao_pretendida == PILHA[-2]:
                #PILHA.pop()
                DIRECAO_CAMINHADA.append(dir)
                PILHA.pop()
                return True

        # for dir in DIRECOES:
        #     posicao_pretendida = [list(posicao)[0] + dir[0], list(posicao)[1] + dir[1]]
        #     if LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == CAMINHO_PERCORRIDO:
        #         DIRECAO_TESTADA.append(dir)

        #         return True     

    elif (
        LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == CAMINHO_LIVRE 
        or LABIRINTO[posicao_pretendida[0]][posicao_pretendida[1]] == SAIDA):
        DIRECAO_CAMINHADA.append(direcao)
        return True


def main():

    POSICAO_INICIAL = [8, 6]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    POSICAO_ATUAL = POSICAO_INICIAL

    PILHA.append(POSICAO_INICIAL)
    
    while POSICAO_ATUAL != INDICE_SAIDA:
    
        for direcao_caminhada in DIRECOES:

            if POSICAO_ATUAL == INDICE_SAIDA:
                break

            elif verifica_movimento(POSICAO_ATUAL, direcao_caminhada):
                direcao_caminhada = DIRECAO_CAMINHADA[0]
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, direcao_caminhada)
                print_labirinto()
                sleep(0.5)
                DIRECAO_CAMINHADA.pop()
                

    print(PILHA)
    print(f'\n{"*"*60}\n\tO jogo terminou, o robô achou a saída!\n{"*"*60}')

if __name__ == "__main__":
    main()
