def menu():
    while True:
        print('\nMENU INICIAL')
        print('Selecione uma opção:\n')
        print('1. Realizar pesquisa')
        print('2. Verificar tempo de carregamento das estruturas')
        print('3. Sair')

        opcao = input('\n> ')
        if(opcao.isnumeric() and (opcao >= '1' and opcao <= '3')):
            opcao = int(opcao)
            break
        else:
            print('\nPor favor, selecione uma opção válida de entrada.\n')
    
    return opcao


def imprimeFormatos():
    print('\nOs formatos de pesquisa são:')
    print("Pesquisar jogadores pelo nome: player <name or prefix>")
    print("Pesquisar jogadores revisados por um usuário: user <userID>")
    print("Pesquisar jogadores por posição: top<N> ‘<position>’")
    print("Pesquisar jogadores por tags: tags <list of tags>")


def imprimeTempos(tempo_carregamento):
    print(f'\nTempo carregamento jogadores: {tempo_carregamento[1]}')
    print(f'Tempo carregamento usuários: {tempo_carregamento[2]}')
    print(f'Tempo carregamento posições: {tempo_carregamento[3]}')
    print(f'Tempo carregamento tags: {tempo_carregamento[4]}')
    print(f'Tempo carregamento nomes: {tempo_carregamento[5]}')
    print(f'Tempo total de carregamentos: {tempo_carregamento[0]}')