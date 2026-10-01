from utils import leitura_arquivo
from Grafo import Grafo

vertices, arestas, matriz_adjacencia = leitura_arquivo('grafoteste.txt')

grafo = Grafo(vertices=vertices, arestas=arestas, matriz=matriz_adjacencia)

vizinhos_vertice = grafo.vizinhos(1)

grafo.print_matriz()

print(vizinhos_vertice)
grafo.encontrar_articulacoes()
