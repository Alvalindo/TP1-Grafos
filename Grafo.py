from collections import deque

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
                
                vizinhos.append(i + 1)

        return vizinhos

    #para saber o grau é so contar os vizinhos
    def grau_vertice(self, vertice):
        return len(self.vizinhos(vertice=vertice))

    #funcao utilitaria de busca em profundidade
    def busca_em_profundidade(self, atual, visitado, removido=-1):
            visitado[atual] = True
    
            for vizinho in range(self.vertices):
                if (vizinho != removido
                        and self.matriz[atual][vizinho] != 0
                        and not visitado[vizinho]):
    
                    self.busca_em_profundidade(vizinho, visitado, removido)
    
    #funcao utilitaria que usa a busca em profudidade para contar os componentes
    def contar_componentes(self, removido=-1):
        n = self.vertices
        visitado = [False] * n
        componentes = 0

        for v in range(n):
            if v != removido and not visitado[v]:
                componentes += 1
                self.busca_em_profundidade(v, visitado, removido)

        return componentes

    #returna true para um vertice que é articulacao e false para um que não é
    def vertice_eh_articulacao(self, vertice):
        v1 = self.contar_componentes(vertice-1)
        v2 = self.contar_componentes()

        return True if v1 > v2 else False

    #algoritmo de busca em largura, usando fila. retorna a sequencia de vertices visitados e as arestas de retorno
    def busca_largura(self, vertice):
            vertice = vertice - 1

            visitados = [False] * self.vertices
            
            fila = deque([vertice])
            visitados[vertice] = True
            
            sequencia_visitados = []
            arestas_arvore = set()
            todas_arestas = set()
            
            #mapeia todas as arestas unicas do grafo
            for i in range(self.vertices):
                for j in range(i, self.vertices):
                    if self.matriz[i][j] != 0:
                        todas_arestas.add((i, j))
                        
            while fila:
                vertice_atual = fila.popleft()
                sequencia_visitados.append(vertice_atual)
                
                for vizinho in range(self.vertices):
                    if self.matriz[vertice_atual][vizinho] != 0:
                        if not visitados[vizinho]:
                            visitados[vizinho] = True
                            fila.append(vizinho)
                            
                            aresta_arvore = (min(vertice_atual, vizinho), max(vertice_atual, vizinho))
                            arestas_arvore.add(aresta_arvore)
    
            # descobrimos as arestas que nao fazem parte
            arestas_retorno = todas_arestas - arestas_arvore

            #convertendo para vertices com base 1
            sequencia_visitados = [v + 1 for v in sequencia_visitados]
            arestas_retorno = sorted((a + 1, b + 1) for a, b in arestas_retorno)
            
            return sequencia_visitados, list(arestas_retorno)

    #funcao de verificar quanto componentes conexo ha no grafo
    def componentes_conexas(self):
        n = self.ordem()

        #copia a matriz de adjacencia
        matriz = [linha[:] for linha in self.matriz]

        #roy-warshall: gera a matriz de alcancabilidade
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matriz[i][k] != 0 and matriz[k][j] != 0:
                        matriz[i][j] = 1

        #o vertice é alcancavel por ele mesmo
        for i in range(n):
            matriz[i][i] = 1

        #descobre os componentes
        visitados = [False] * n
        componentes = []

        for i in range(n):
            if not visitados[i]:
                componente = []
                for j in range(n):
                    if matriz[i][j] != 0:
                        componente.append(j + 1)
                        visitados[j] = True

                componentes.append(componente)

        print("Número de componentes:", len(componentes))

        for i, componente in enumerate(componentes, 1):
            print(f"Componente {i}: {componente}")

    #funcao auxiliar de busca em profundidade adaptada para detectar ciclos
    def bp_ciclo(self, vertice_atual, visitados, vertice_pai):
        visitados[vertice_atual] = True

        lista_vizinhos = self.vizinhos(vertice_atual + 1)

        for vizinho in lista_vizinhos:
            vizinho_index = vizinho - 1

            if visitados[vizinho_index] == False:
                if self.bp_ciclo(vizinho_index, visitados, vertice_atual):
                    return True
                
            elif vizinho_index != vertice_pai:
                return True # encontrou ciclo
            
        return False

    #verifica se o grafo possui ciclo usando busca em profundidade
    def possui_ciclo(self):
        ordem = self.ordem()
        visitados = [False] * ordem

        for i in range(ordem):
            if(visitados[i] == False):
                if self.bp_ciclo(i, visitados, -1):
                    return True
                
        return False
        
    #calcula o menor caminho de uma origem para todos os vertices usando dijkstra. devolve uma lista de tuplas no formato (vertice predecessor, distancia).
    def caminhos_minimos(self, vertice):
        origem_index = vertice - 1
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
            for i in lista_vizinhos:
                if (F[i - 1] == False):
                    V.append((i, self.matriz[r][i - 1]))   
            for i, peso in V:
                p = min(dt[i - 1], dt[r] + peso)
                if (p < dt[i - 1]):
                    dt[i - 1] = p
                    rot[i - 1] = r 
        resultado = []
        for v in range(ordem):
            #guardando o par (pai, distancia) para cada vertice
            if rot[v] != float('inf') and rot[v] != -1:
                rot_usuario = rot[v] + 1
            else:
                rot_usuario = float('inf')
            resultado.append((rot_usuario, dt[v]))
            
        return resultado

    #pega a distancia exata e a rota entre dois vertices. usa o resultado do menor_caminho e reconstroi o trajeto de tras pra frente usando os predecessores.
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