class Grafo():

    #construtor da classe grafo
    def __init__(self, vertices, arestas, matriz):
        self.vertices = vertices
        self.arestas = arestas
        self.matriz = matriz


    #retorna o numero de vertices
    def ordem(self):
        return self.vertices

    #retorna o numero de arestas
    def tamanho(self):
        return self.arestas

    #retorna a densidade, ou seja: (2.n_arestas) / (vertices.(vertices-1))
    def densidade(self):
        num_arestas = self.tamanho()
        num_vertices = self.ordem()

        densidade = (2 * num_arestas) / ((num_vertices)*(num_vertices - 1))

        return densidade

    #pega os vizinhos. a logica é: se o vertice atual, junto com o vertice do for, tiver peso diferente de 0, sao vizinhos.
    def vizinhos(self, vertice):
        index = vertice - 1

        vizinhos = []

        for i in range(self.vertices):
            if (self.matriz[index][i] != 0 and
               self.matriz[i][index] != 0 and
               self.matriz[i][index] == self.matriz[index][i]):
                
                vizinhos.append((i + 1, self.matriz[index][i]))

        return vizinhos

    #para saber o grau é so contar os vizinhos
    def grau_vertice(self, vertice):
        return len(self.vizinhos(vertice=vertice))

    #a ser implementado
    def vertice_eh_articulacao(self, vertice):
        pass

    #a ser implementado
    def busca_largura(vertice):
        pass

    #a ser implementado
    def componentes_conexas(self):
        pass

    # verifica se o grafo possui ciclo usando busca em profundidade
    def possui_ciclo(self):
        ordem = self.ordem()
        visitados = [False] * ordem
        for i in range(ordem):
            if(visitados[i] == False):
                if self.bp_ciclo(i, visitados, -1):
                    return True
        return False

    # funcao auxiliar de busca em profundidade para detectar ciclos
    def bp_ciclo(self, vertice_atual, visitados, vertice_pai):
        visitados[vertice_atual] = True
        lista_vizinhos = self.vizinhos(vertice_atual + 1)
        for vizinho, peso in lista_vizinhos:
            vizinho_index = vizinho - 1
            if visitados[vizinho_index] == False:
                if self.bp_ciclo(vizinho_index, visitados, vertice_atual):
                    return True
            elif vizinho_index != vertice_pai:
                return True # Encontrou ciclo
        return False
        
    #a ser implementado
    def menor_caminho():
        pass


    #funcao auxiliar para vizualizar a matriz de adjacencia
    def print_matriz(self):
        for i in range(self.vertices):
            linha = [f"{self.matriz[i][j]:.1f}" for j in range(self.vertices)]
            print(" ".join(linha))
