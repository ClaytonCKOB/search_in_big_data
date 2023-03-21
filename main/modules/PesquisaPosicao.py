from main.modules.salva import mapHash, mapHashNum
from .classe import *


def pesquisaPosicao(Tabela_jogadores, Tabela_posicoes, posicao, tam):
    pos = mapHash(posicao, Tam_posicoes)

    if(Tabela_posicoes[pos]):   #Caso encontre a o endereço na tabela Hash de posições, percorre a lista no endereço
        response = []
        print("\n{:<15} {:<50} {:<25} {:<20} {:<15}".format('fifa_id','name','player_position', 'rating', 'count'))
        for i in range(len(Tabela_posicoes[pos])):
            if(Tabela_posicoes[pos][i].posicao == posicao): #Caso encontre a posição
                ordenaPosicoes(Tabela_posicoes[pos][i].ids, Tabela_jogadores)   #Ordena as avaliações do vetor de ids de jogadores que jogam nessa posição utilizando Shell Sort
                for j in range(tam):
                    if(j < len(Tabela_posicoes[pos][i].ids)):
                        pos_jogador = mapHashNum(Tabela_posicoes[pos][i].ids[j], Tam_jogadores)
                        for k in range(len(Tabela_jogadores[pos_jogador])):
                            if(Tabela_jogadores[pos_jogador][k].fifa_id == Tabela_posicoes[pos][i].ids[j]): #Quando encontrou o id do vetor de posições na tabela Hash de jogadores
                                if(Tabela_jogadores[pos_jogador][k].num >= 1000):   #Caso o jogador tenha 1000 ou mais avaliações recebidas, imprime suas informações
                                    if(Tabela_jogadores[pos][k].num != 0):
                                        rating = Tabela_jogadores[pos_jogador][k].nota / Tabela_jogadores[pos_jogador][k].num
                                    else:
                                        rating = 0.0
                                    response.append({
                                        'fifa_id':Tabela_jogadores[pos_jogador][k].fifa_id,
                                        'name': Tabela_jogadores[pos_jogador][k].nome,
                                        'player_positions': ', '.join(Tabela_jogadores[pos_jogador][k].posicao),
                                        'rating': round(rating, 2),
                                        'count': Tabela_jogadores[pos_jogador][k].num
                                    })

        return response
    else:
        return []

def ordenaPosicoes(ids, Tabela_jogadores):
    seq = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]
    shellSort(ids, seq, Tabela_jogadores)


def shellSort(C, ordem, Tabela_jogadores):
    #Procura a posição no vetor dos tamanhos de segmentos
    for j in range(0, len(ordem), 1):
        if ordem[j] >= len(C):
            posicaoOrdem = j-1
            break
    
    #Chama a função de Inserção Direta passando o tamanho do incremento de segmento
    for j in range(posicaoOrdem, -1, -1):
        h = ordem[j]
        insertion_sort(C, h, Tabela_jogadores)


def insertion_sort(C, h, Tabela_jogadores):
    for i in range(h, len(C)):
        chave = C[i]
        j = i - h

        while(j>=0 and calculaNota(chave, Tabela_jogadores) > calculaNota(C[j], Tabela_jogadores)):
            C[j+h] = C[j]
            j -= h
    
        C[j+h] = chave


def calculaNota(id, Tabela_jogadores):
    pos = mapHashNum(id, Tam_jogadores)    
    for i in range(len(Tabela_jogadores[pos])):  
        if (Tabela_jogadores[pos][i].fifa_id == id):
            if(Tabela_jogadores[pos][i].num != 0):
                media =  Tabela_jogadores[pos][i].nota / Tabela_jogadores[pos][i].num
            else:
                media = 0.0
            return media

                
        


            

