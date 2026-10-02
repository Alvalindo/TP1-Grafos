from utils import validar_vertice, iniciar_programa

grafo = iniciar_programa()

count_iteracoes = 0

while True:
    if count_iteracoes == 0 or count_iteracoes > 4:
        count_iteracoes = 0

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

    opcao_grafo = opcao_inicial = int(input('\nDigite a opção: '))

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
            print('Saindo...')
            break

        case _:
            print('Opção inválida!')
            count_iteracoes +=1