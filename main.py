from utils import validar_vertice, iniciar_programa, printar_menu

grafo = iniciar_programa()

count_iteracoes = 0

while True:
    if count_iteracoes == 0 or count_iteracoes > 4:
        count_iteracoes = 0

        printar_menu()

    opcao_grafo = int(input('\nDigite a opção: '))

    match opcao_grafo:
        case 0:
            grafo = iniciar_programa(1)
            count_iteracoes = 0

        case 1:
            print(f'Ordem do grafo: {grafo.ordem()}')
            count_iteracoes +=1


        case 2:
            print(f'Tamanho do grafo: {grafo.tamanho()}')
            count_iteracoes +=1

        case 3:
            print(f'Densidade do grafo: {grafo.densidade():.2f}')
            count_iteracoes +=1

        case 4:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber seus vizinhos: '))
            if not validar_vertice(vertice, grafo.ordem()):
                print('Vértice inválido!')

            print(f'Vértices vizinhos do vértice {vertice}: {grafo.vizinhos(vertice)}')
            count_iteracoes +=1

        case 5:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber seu grau: '))
            if not validar_vertice(vertice, grafo.ordem()):
                print('Vértice inválido!')
            
            print(f'Grau do vértice {vertice}: {grafo.grau_vertice(vertice)}')
            count_iteracoes +=1

        case 6:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber se ele é ou não articulação: '))
            if not validar_vertice(vertice, grafo.ordem()):
                print('Vértice inválido!')

            eh_articulacao = grafo.vertice_eh_articulacao(vertice)
            print('O vértice é articulação!' if eh_articulacao else 'O vértice não é articulação')
            count_iteracoes +=1

        case 7:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice origem: '))
            if not validar_vertice(vertice, grafo.ordem()):
                print('Vértice inválido!')

            sequencia_visitados, arestas_retorno = grafo.busca_largura(vertice)

            print(f'Sequência de vértices visitados: {sequencia_visitados}')
            print(f'Arestas de retorno (não fazem parte da árvore de busca): {arestas_retorno}')
            count_iteracoes +=1

        case 8:
            grafo.componentes_conexas()
            count_iteracoes +=1

        case 9:
            ciclo = grafo.possui_ciclo()

            print('Sim, grafo possui ciclo' if ciclo else 'Não, grafo não possui ciclo.')
            count_iteracoes +=1

        case 10:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice origem: '))
            if not validar_vertice(vertice, grafo.ordem()):
                print('Vértice inválido!')

            lista_caminhos = grafo.caminhos_minimos(vertice)

            print(f'Caminhos mínimos: {lista_caminhos}')
            count_iteracoes +=1
            
        case 11:
            vertice_origem = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice origem: '))
            if not validar_vertice(vertice_origem, grafo.ordem()):
                print('Vértice origem inválido!')
                count_iteracoes += 1
                continue

            vertice_destino = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice destino: '))
            if not validar_vertice(vertice_destino, grafo.ordem()):
                print('Vértice destino inválido!')
                count_iteracoes += 1
                continue

            distancia, caminho = grafo.distancia_dois_vertices(vertice_origem, vertice_destino)
            if distancia == float('inf'):
                print(f'\nNão existe caminho alcançável entre o vértice {vertice_origem} e o vértice {vertice_destino}.')
            else:
                print(f'\nDistância do vértice {vertice_origem} ao vértice {vertice_destino}: {distancia}')
                print(f'Caminho percorrido: {caminho}')
            count_iteracoes += 1

        case 12:
            print('Saindo...')
            break

        case _:
            print('Opção inválida!')
            count_iteracoes +=1