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


    def busca_em_profundidade(self, atual, visitado, removido=-1):
        visitado[atual] = True

        for vizinho in range(self.vertices):
            if (vizinho != removido
                    and self.matriz[atual][vizinho] != 0
                    and not visitado[vizinho]):

                self.busca_em_profundidade(vizinho, visitado, removido)


    def contar_componentes(self, removido=-1):
        n = self.vertices
        visitado = [False] * n
        componentes = 0

        for v in range(n):
            if v != removido and not visitado[v]:
                componentes += 1
                self.busca_em_profundidade(v, visitado, removido)

        return componentes


    def encontrar_articulacoes(self):
        original = self.contar_componentes()
        articulaçoes = []
        count = 0

        for v in range(self.vertices):
            depois = self.contar_componentes(v)

            if depois > original:
                articulaçoes.append(v + 1)

        if articulaçoes == []:
            print("Não há vértices de articulação.")

        else :
            print("Vértices de articulação:")
            print(articulaçoes)
                
