from django.http import JsonResponse
from main.modules.PesquisaPosicao import pesquisaPosicao
from main.modules.PesquisaTag import pesquisaTag
from main.modules.salva import abreArquivos
from main.modules.PesquisaUsuarios import pesquisaUsuario
from main.modules.PesquisaPosicao import pesquisaPosicao
from main.modules.PesquisaNome import pesquisaNome
from main.modules.classe import *
from main.modules.menu import *
from main.modules.consts import *
import main.modules.consts as const
import time, json

def loadFiles(response):
    inicio = time.time()
    const.mainNode = abreArquivos(Tabela_jogadores, Tabela_usuarios, Tabela_posicoes, Tabela_tags, tempo_carregamento)
    fim = time.time()
    return JsonResponse({"time": (fim - inicio)/60})

def userSearch(response):
    user_id = int(response.GET.get('user_id'))
    players = pesquisaUsuario(Tabela_jogadores, Tabela_usuarios, user_id)
    return JsonResponse({"players": json.dumps(players)})

def tagsSearch(response):
    tags = response.GET.get('tags') 
    pesquisaTag(Tabela_jogadores, Tabela_tags, tags)

def topSearch(response):
    tam = response.GET.get('top')
    posicao = response.GET.get('posicao')
    tam = int(tam[1])
    pesquisaPosicao(Tabela_jogadores, Tabela_posicoes, posicao, tam)


def playerSearch(response):
    prefixo = response.GET.get('prefixo').lower()
    players = pesquisaNome(Tabela_jogadores, const.mainNode, prefixo)
    return JsonResponse({"players": json.dumps(players)})