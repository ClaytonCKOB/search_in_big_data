from main.modules.classe import Tam_jogadores
from main.modules.trie import *
from main.modules.salva import mapHashNum
from .PesquisaPosicao import ordenaPosicoes

def pesquisaNome(Tabela_jogadores, trie, prefixo):
    ids = trie.searchJogador(prefixo) #Extrai os ids com o prefixo da árvore trie
    if(ids): #Caso encontre os ids do prefixo
        for i in range(len(ids)):
            ids[i] = int(ids[i])
        return encontraJogadores(ids, Tabela_jogadores)
    else:
        return []


def encontraJogadores(ids, Tabela_jogadores):
    ordenaPosicoes(ids, Tabela_jogadores)

    print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format('sofifa_id','name','player_positions', 'rating', 'count'))
    response = []
    #Imprime cada jogador de cada id extraido da árvore trie
    for i in range(len(ids)):
        pos = mapHashNum(ids[i], Tam_jogadores)

        for j in range(len(Tabela_jogadores[pos])):
            if(Tabela_jogadores[pos][j].fifa_id == ids[i]): #Ao encontrar o id do jogador na tabela Hash de jogadores, imprime suas informações
                if(Tabela_jogadores[pos][j].num != 0):
                    rating = Tabela_jogadores[pos][j].nota / Tabela_jogadores[pos][j].num
                else:
                    rating = 0.0
                response.append({
                    'sofifa_id':Tabela_jogadores[pos][j].fifa_id,
                    'name': Tabela_jogadores[pos][j].nome,
                    'player_positions': ', '.join(Tabela_jogadores[pos][j].posicao),
                    'rating': rating,
                    'count': Tabela_jogadores[pos][j].num
                })
                # print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format(Tabela_jogadores[pos][j].fifa_id, Tabela_jogadores[pos][j].nome, ', '.join(Tabela_jogadores[pos][j].posicao), rating, Tabela_jogadores[pos][j].num))

    
    return response