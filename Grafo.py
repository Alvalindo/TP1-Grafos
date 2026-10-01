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
            if self.matriz[index][i] != 0:
                vizinhos.append(i + 1)

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

    #a ser implementado
    def possui_ciclo(self):
        pass

    #a ser implementado
    def menor_caminho():
        pass


    #funcao auxiliar para vizualizar a matriz de adjacencia
    def print_matriz(self):
        for i in range(self.vertices):
            linha = [f"{self.matriz[i][j]:.1f}" for j in range(self.vertices)]
            print(" ".join(linha))
