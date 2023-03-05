from .classe import *
from .trie import *
import csv
import time


def abreArquivos(Tabela_jogadores, Tabela_usuarios, Tabela_posicoes, Tabela_tags, tempo_carregamento):
    
    inicio = time.time()
    arquivo = open('main/files/players.csv', mode='r')
    jogadores = csv.reader(arquivo)
    salvaJogadores(Tabela_jogadores, jogadores)
    arquivo.close()
    fim = time.time()
    tempo_carregamento[1] = fim - inicio
    
    inicio = time.time()
    arquivo = open('main/files/rating.csv', mode='r')
    usuarios = csv.reader(arquivo)
    salvaUsuarios(Tabela_jogadores, Tabela_usuarios, usuarios)
    arquivo.close()
    fim = time.time()
    tempo_carregamento[2] = fim - inicio

    inicio = time.time()
    arquivo = open('main/files/players.csv', mode='r')
    jogadores = csv.reader(arquivo)
    salvaPosicoes(Tabela_posicoes, jogadores)
    arquivo.close()
    fim = time.time()
    tempo_carregamento[3] = fim - inicio

    inicio = time.time()
    arquivo = open('main/files/tags.csv', mode='r')
    tags = csv.reader(arquivo)
    salvaTags(Tabela_tags, tags)
    arquivo.close()
    fim = time.time()
    tempo_carregamento[4] = fim - inicio

    inicio = time.time()
    arquivo = open('main/files/players.csv', mode='r')
    nomes = csv.reader(arquivo)
    mainNode = loadJogadores(nomes)
    arquivo.close()
    fim = time.time()
    tempo_carregamento[5] = fim - inicio

    return mainNode

#Percorre o arquivo de jogadores extraindo id, nome e posições
def salvaJogadores(tabela, jogadores):
    next(jogadores) 
    for linha in jogadores:
        id = int(linha[0])
        nome = linha[1]
        posicoes = linha[2].split(', ')
        hashJogador(tabela, id, nome, posicoes)


def hashJogador(tabela, id, nome, posicoes):
    pos = mapHashNum(id, Tam_jogadores)
    
    if(tabela[pos]):
        tabela[pos].append(Jogador(id, nome, posicoes)) #Caso já tenha um jogador na lista do endereço, adiciona um novo
    else:
        tabela[pos] = []
        tabela[pos].append(Jogador(id, nome, posicoes)) #Caso não tenha, cria a lista

#Percorre o arquivo de ratings extraindo id do jogador, id do usuário e nota dada
def salvaUsuarios(tabela_jogadores, tabela_usuarios, usuarios):
    next(usuarios)
    for linha in usuarios:
        user_id = int(linha[0])
        player_id = int(linha[1])
        nota = float(linha[2])
        hashRating(tabela_jogadores, player_id, nota)
        hashUsuario(tabela_usuarios, user_id, player_id, nota)


def hashRating(tabela, id, nota):
    pos = mapHashNum(id, Tam_jogadores)
    
    if(tabela[pos]):
        for i in range(len(tabela[pos])):
            if(tabela[pos][i].fifa_id == id):
                tabela[pos][i].nota += nota #Caso tenha encontrado o jogador, soma a nota recebida ao total de suas notas
                tabela[pos][i].num += 1     #Soma 1 no contador de avaliações recebidas


def hashUsuario(tabela, user_id, player_id, nota):
    pos = mapHashNum(user_id, Tam_usuarios)

    if(tabela[pos]):
        addUsuario(tabela[pos], user_id, player_id, nota)   #Caso já tenha usuário na lista do endereço, checa se o usuário já está na lista
    else:
        tabela[pos] = []
        addUsuario(tabela[pos], user_id, player_id, nota)   #Caso não tenha, cria a lista e adiciona o usuário  


def addUsuario(lista, user_id, player_id, nota):
    if(lista):
        for i in range(len(lista)):
            if(lista[i].id == user_id):
                novaNota(lista[i].notas, player_id, nota)   #Se encontrou o usuário na lista, adiciona um nova avalição ao seu vetor de notas
                return
        criaUsuario(lista, user_id, player_id, nota)        #Caso não tenha encontrado, cria um novo usuário para adicionar à lista de usuários
    else:
        criaUsuario(lista, user_id, player_id, nota)        #Caso não tenha usuários na lista, cria o primeiro usuário para ser adicionado à lista
        

def criaUsuario(lista, user_id, player_id, nota):
    novo_usuario = Usuario(user_id)
    novaNota(novo_usuario.notas, player_id, nota)
    lista.append(novo_usuario)

#Adiciona nota e id do jogador avaliado ao vetor de notas do usuário
def novaNota(notas, id, nota):
    nova_aval = Notas(id, nota)
    notas.append(nova_aval)

#Percorre arquivo de jogadores extraindo id do jogador e posições
def salvaPosicoes(tabela, jogadores):
    next(jogadores)
    for linha in jogadores:
        id = int(linha[0])
        posicoes = linha[2].split(', ')
        hashPosicoes(tabela, id, posicoes)



def hashPosicoes(tabela, id, posicoes):
    for i in range(len(posicoes)):
        pos = mapHash(posicoes[i].lower(), Tam_posicoes)
        if(tabela[pos]): #Caso já tenha uma posição na lista do endereço, percorre a lista procurando a posição do jogador
            for j in range(len(tabela[pos])):
                if(tabela[pos][j].posicao == posicoes[i].lower()):
                    if(id not in tabela[pos][j].ids):
                        tabela[pos][j].ids.append(id)   #Caso não tenha encontrado o id do jogador no vetor de ids da posição, adiciona ele
        else:   #Caso não tenha uma lista no endereço
            nova_posicao = Posicao(posicoes[i].lower().strip())
            nova_posicao.ids.append(id)
            tabela[pos] = []
            tabela[pos].append(nova_posicao)    #Cria a lista da posição, cria uma nova posição e adiciona o id do jogador ao vetor de ids da posição

#Percorre o arquivo de tags extraindo id do jogador e tag atribuida a ele
def salvaTags(tabela, tag):
    next(tag)
    for linha in tag:
        id = int(linha[1])
        tag = linha[2]
        hashTags(tabela, id, tag)


def hashTags(tabela, id, tag):
    pos = mapHash(tag.lower(), Tam_tags)
    if(tabela[pos]):    #Caso tenha encontrado uma tag na lista do endereço, percorre a lista procurando a tag do jogador
        for j in range(len(tabela[pos])):     
                if(tabela[pos][j].tag == tag.lower()):   #Caso tenha encontrado a tag do jogador na lista     
                    if id not in tabela[pos][j].ids:   
                        tabela[pos][j].ids.append(id)   #Caso não tenha encontrado o id do jogador no vetor de ids da tag, adiciona ele 
    else:   #Caso não tenha uma lista no endereço
        if isinstance(tag, str):
            nova_tag = Tag(tag.lower())            
            nova_tag.ids.append(id)
            tabela[pos] = []
            tabela[pos].append(nova_tag)    #Cria a lista da posição, cria uma nova tag e adiciona o id do jogador ao vetor de ids da tag
        

def mapHashNum(id, tam):
    return id % tam


def mapHash(chave, tam):             
    soma = 0
    p = 127
    for i in range(len(chave)):
        soma += ord(chave[i]) * (p**i)
    return soma % tam

