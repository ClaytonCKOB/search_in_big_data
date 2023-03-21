from ast import Return
from .salva import mapHashNum
from .classe import *


def pesquisaUsuario(Tabela_jogadores, Tabela_usuarios, user_id):
    pos = mapHashNum(user_id, Tam_usuarios)

    if(Tabela_usuarios[pos]):   #Procura o id do usuário na tabela Hash de usuários
        for i in range(len(Tabela_usuarios[pos])):
            if(Tabela_usuarios[pos][i].id == user_id): #Caso encontre o id do usuário na tabela
                ordenaAvals(Tabela_usuarios[pos][i].notas)  #Ordena suas avaliações usando Shell Sort
                return encontraJogadores(Tabela_usuarios[pos][i].notas, Tabela_jogadores)
        return []
    else:
        return []


def encontraJogadores(avals, Tabela_jogadores):
    limite = 0
    response = []

    #Imprime os 20 jogadores melhores avaliados pelo usuário
    while(limite < len(avals) and limite < 20):
        player_id = avals[limite].fifa_id
        player_rating = avals[limite].nota
        pos = mapHashNum(player_id, Tam_jogadores)

        if(Tabela_jogadores[pos]):
            for i in range(len(Tabela_jogadores[pos])):
                if(Tabela_jogadores[pos][i].fifa_id == player_id):  #Quando encontrar o id do jogador, imprime suas informações
                    name = Tabela_jogadores[pos][i].nome
                    count = Tabela_jogadores[pos][i].num
                    global_ranking = (Tabela_jogadores[pos][i].nota) / count
                    response.append({
                        'sofifa_id':player_id,
                        'name': name,
                        'global_rating': round(global_ranking, 2),
                        'count': count,
                        'rating': player_rating
                    })
                    # print("{:<15} {:<40} {:<15.6} {:<15} {:<15}".format(player_id, name, global_ranking, count, player_rating))
        limite += 1
    
    return response


def ordenaAvals(avals):
    seq = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711] #ciura
    shellSort(avals, seq)


def shellSort(C, ordem):
    #Procura a posição no vetor dos tamanhos de segmentos
    for j in range(0, len(ordem), 1):
        if ordem[j] >= len(C):
            posicaoOrdem = j-1
            break
    
    #Chama a função de Inserção Direta passando o tamanho do incremento de segmento
    for j in range(posicaoOrdem, -1, -1):
        h = ordem[j]
        insertion_sort(C, h)


def insertion_sort(C, h):
    for i in range(h, len(C)):
        chave = C[i]
        j = i - h

        while(j>=0 and chave.nota > C[j].nota):
            C[j+h] = C[j]
            j -= h
    
        C[j+h] = chave



