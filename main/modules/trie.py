class Node:
    def __init__(self, id):
        self.ids = []
        if id != -1:
            self.ids.append(id)
        self.nodes = [None] * 31

    def __getitem__(self, i):
        if len(self.nodes) >= i:
            return self.nodes[i]
        else:
            return None

    def __setitem__(self, i, node):
        self.nodes[i] = node

    # Verifica se o nodo é o final de algum nome
    def hasIds(self):
        return len(self.ids) > 0

    # Busca algum jogador a partir do seu prefixo do nome
    def searchJogador(self, prefix):
        next = self
        print(prefix)
        for c in prefix:
            index = getCharValue(c)
            if next[index]:
                next = next[index]
            else:
                return []

        return next.findAllValues()

    # Ao encontrar um nodo pela função acima, faz uma busca recursiva em seus filhos
    # e os adiciona em uma lista contendo todos IDs encontrados
    def findAllValues(self):
        list = []
        if self.hasIds():
            for id in self.ids:
                list.append(id)

        for n in self.nodes:
            if n is not None:
                for id in n.findAllValues():
                    list.append(id)

        return list

# Carrega a árvore trie e retorna o nodo base da árvore
def loadJogadores(tabela_jogadores):
    #next(tabela_jogadores)
    node = Node(-1)
    for linha in tabela_jogadores:
        id = linha[0]
        name = linha[1]
        last_node = node
        for c in name:
            index = getCharValue(c)
            if not last_node[index]:
                last_node[index] = Node(-1)
            last_node = last_node[index]
        last_node.ids.append(id)
    return node


# Retorna o valor de cada letra e alguns casos extras que não estão
# na sequencia da tabela ascii, como '"' e '.'
def getCharValue(char):
    if char == ' ':
        return 26
    elif char == '-':
        return 27
    elif char == '\'':
        return 28
    elif char == '.':
        return 29
    elif char == '"':
        return 30
    else:
        return ord(char.lower()) - 97

