#Função para fazer a leitura do grafo e traforma-lo em uma matriz de adjacência

def leitura_arquivo(nome_arquivo):

    with open(nome_arquivo, "r") as arquivo:

        quantidade_vertices = int(arquivo.readline())

        matriz = [[float(0)] * quantidade_vertices for i in range(quantidade_vertices)]

        quantidade_arestas = 0

        for linha in arquivo:

            lista_linha = linha.split()

            origem = int(lista_linha[0]) - 1
            destino = int(lista_linha[1]) - 1
            peso = float(lista_linha[2])

            matriz[origem][destino] = peso
            matriz[destino][origem] = peso

            quantidade_arestas += 1

    return quantidade_vertices, quantidade_arestas, matriz


