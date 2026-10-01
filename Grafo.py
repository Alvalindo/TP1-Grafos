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
        
    #calcula o menor caminho de uma origem para todos os vertices usando dijkstra.
    #devolve uma lista de tuplas no formato (vertice predecessor, distancia).
    def caminhos_minimos(self, origem):
        origem_index = origem - 1
        ordem = self.ordem()
        dt = [float('inf')] * ordem
        rot = [-1] * ordem
        rot[origem_index] = float('inf')
        dt[origem_index] = 0
        F = [False] * ordem
        A = [True] * ordem
        for _ in range(ordem):
            menor_dt = float('inf')
            r = -1
            for v in range(ordem):
                if (A[v] == True):
                    if (dt[v] < menor_dt):
                        menor_dt = dt[v]
                        r = v
            if r == -1:
                break
            F[r] = True
            A[r] = False
            V = []
            lista_vizinhos = self.vizinhos(r + 1)
            for i, peso in lista_vizinhos:
                if (F[i - 1] == False):
                    V.append((i, peso))   
            for i, peso in V:
                p = min(dt[i - 1], dt[r] + peso)
                if (p < dt[i - 1]):
                    dt[i - 1] = p
                    rot[i - 1] = r 
        resultado = []
        for v in range(ordem):
            # Guardando o par (pai, distancia) para cada vértice
            if rot[v] != float('inf') and rot[v] != -1:
                rot_usuario = rot[v] + 1
            else:
                rot_usuario = float('inf')
            resultado.append((rot_usuario, dt[v]))
        return resultado

    #pega a distancia exata e a rota entre dois vertices. 
    #logica: usa o resultado do menor_caminho e reconstroi o trajeto de tras pra frente usando os predecessores.
    def distancia_dois_vertices(self, origem, destino):
        resultado = self.caminhos_minimos(origem)
        destino_index = destino - 1
        predecessor, distancia = resultado[destino_index]
        caminho = []
        percorre = destino
        while percorre != origem:
            caminho.append(percorre)
            predecessor, _ = resultado[percorre - 1]

            if (predecessor == float('inf')):
                return float('inf'), []
            percorre = predecessor
        caminho.append(origem)
        caminho.reverse()
        return distancia, caminho


    #funcao auxiliar para vizualizar a matriz de adjacencia
    def print_matriz(self):
        for i in range(self.vertices):
            linha = [f"{self.matriz[i][j]:.1f}" for j in range(self.vertices)]
            print(" ".join(linha))
