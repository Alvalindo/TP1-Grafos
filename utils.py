import sys
import os
from grafo import Grafo

#Função para fazer a leitura do grafo e traforma-lo em uma matriz de adjacência
def leitura_arquivo(nome_arquivo):
    nome_arquivo = os.path.join('arquivos_teste', nome_arquivo)
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


def carregar_grafo():
    arquivo = input('Digite o nome do arquivo de teste (exemplo: grafo_1.txt): \n')
    resultado = leitura_arquivo(arquivo)

    if resultado:
        vertices, arestas, matriz = resultado

        grafo = Grafo(vertices=vertices, arestas=arestas, matriz=matriz)
    
        print('Grafo carregado com sucesso!')

        return grafo

    else:
        sys.exit()


def printar_menu():
    print('\n')
    
    print('0 - Carregar outro grafo')
    print('1 - Informar ordem do grafo')
    print('2 - Informar tamanho do grafo')
    print('3 - Calcular densidade')
    print('4 - Informar vizinhos de um vértice')
    print('5 - Informar grau de um vértice')
    print('6 - Verificar se um vértice é articulação')
    print('7 - Executar busca em largura')
    print('8 - Identificar componentes conexas')
    print('9 - Verificar existência de ciclos')
    print('10 - Calcular caminhos mínimos')
    print('11 - Sair\n')


def iniciar_programa(aux=0):
    if aux == 0: #inicio do programa
        print('\nANÁLISE DE REDE SOCIAL') 
        print('========================================\n')

        print('1 - Inserir arquivo de teste')
        print('2 - Sair \n')

        opcao_inicial = int(input('Digite a opção: \n'))

        match opcao_inicial:
            case 1:
                grafo = carregar_grafo()

                return grafo

            case 2:
                print('Saindo...')
                sys.exit()

    else: #usuario quer carregar outro grafo
        grafo = carregar_grafo()

        return grafo



def validar_vertice(vertice, ordem, minimo=1):
    if vertice > ordem:
        return False

    if vertice < minimo:
        return False

    return True