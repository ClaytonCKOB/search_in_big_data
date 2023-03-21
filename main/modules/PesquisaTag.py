from .salva import mapHash, mapHashNum
from .classe import *
from .PesquisaPosicao import ordenaPosicoes


def pesquisaTag(Tabela_jogadores, Tabela_tags, tags):
    ids_comTag = []
  
    for i in range(len(tags)):  #Procura todas tags recebidas na tabela Hash de tags
        ok = 0
        pos = mapHash(tags[i], Tam_tags)
        print(pos)
        print(Tabela_tags)
        if(Tabela_tags[pos]):
            for j in range(len(Tabela_tags[pos])):
                print(Tabela_tags[pos][j].tag)
                if(Tabela_tags[pos][j].tag == tags[i]): #Caso encontre a tag, coloca o vetor com os ids dos jogadores que têm essa tag em ids_comTag
                    ids_comTag.append(Tabela_tags[pos][j].ids)
                    ok = 1


            if(ok == 0):
                print(f"\nTag '{tags[i]}' não encontrada")
                return []
        else:
           print(f"\nTag '{tags[i]}' não encontrada")
           return []
    if(len(ids_comTag) > 1):    #Caso sejam mais de uma tag, extrai os ids em comum entre todas as tags
        ids_comTag = tagsComum(ids_comTag)
    else:
        ids_comTag = ids_comTag[0]

    ordenaPosicoes(ids_comTag, Tabela_jogadores) #Ordena as avaliações dos ids por ordem de maior rating utilizando Shell Sort
    return imprimeJogadores(ids_comTag, Tabela_jogadores)


def imprimeJogadores(ids, Tabela_jogadores):
    # print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format('sofifa_id','name','player_positions', 'rating', 'count'))
    response = []
    for i in range(len(ids)):
        pos = mapHashNum(ids[i], Tam_jogadores) #Busca os ids dos jogadores na tabela Hash de jogadores e imprime suas informações

        for j in range(len(Tabela_jogadores[pos])):
            if(Tabela_jogadores[pos][j].fifa_id == ids[i]):
                if(Tabela_jogadores[pos][j].num != 0):
                    rating = Tabela_jogadores[pos][j].nota / Tabela_jogadores[pos][j].num
                else:
                    rating = 0.0
                response.append({
                    'sofifa_id':Tabela_jogadores[pos][j].fifa_id,
                    'name': Tabela_jogadores[pos][j].nome,
                    'player_positions': ', '.join(Tabela_jogadores[pos][j].posicao),
                    'rating': round(rating, 2),
                    'count': Tabela_jogadores[pos][j].num
                })
                # print ("{:<15} {:<50} {:<25} {:<20} {:<15}".format(Tabela_jogadores[pos][j].fifa_id, Tabela_jogadores[pos][j].nome, ', '.join(Tabela_jogadores[pos][j].posicao), rating, Tabela_jogadores[pos][j].num))  #Imprime a tabela
                break   
    return response


#Recebe um vetor de vetores com ids, e retorna um vetor possuindo a interseção entre todos os vetores
def tagsComum(ids_comTag):
    comum = []
    
    for i in range(len(ids_comTag[0])):
        count = 0
        for j in range(1, len(ids_comTag)):
            if(ids_comTag[0][i] in ids_comTag[j]):
                count += 1
        if(count == (len(ids_comTag) - 1)):
            comum.append(ids_comTag[0][i])

    return comum


        


