#Função para fazer a leitura do grafo e traforma-lo em uma matriz de adjacência

def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:

            #Lê a primeira linha, onde determina a quantidade de vértice
            quantidade_vertices = int(arquivo.readline())

            #Gera uma matriz de NxN preenchida com 0's
            matriz = [[float(0)] * quantidade_vertices for i in range(quantidade_vertices)]

            quantidade_arestas = 0

            #Percorre todas as linhas até acabar
            for linha in arquivo:

                #Armazena a linha em uma lista, sendo cada indice um valor
                lista_linha = linha.split()

                if not lista_linha:
                    continue

                #Faz um typecast da lista para valores do tipo int e float
                origem = int(lista_linha[0]) - 1
                destino = int(lista_linha[1]) - 1
                peso = float(lista_linha[2])

                #Preenche a matriz de adjacência com suas devidas ligações
                matriz[origem][destino] = peso
                matriz[destino][origem] = peso

                #cada linha representa uma aresta, logo, contabilizando as arestas
                quantidade_arestas += 1

        return quantidade_vertices, quantidade_arestas, matriz
    
    except FileNotFoundError:
        print('Erro: O arquivo não existe!')
        return False


def validar_vertice(vertice, ordem, minimo=1):
    if vertice > ordem:
        return False

    if vertice < minimo:
        return False

    return True