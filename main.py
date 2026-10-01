from utils import leitura_arquivo, validar_vertice
from grafo import Grafo
import sys

print('\nANÁLISE DE REDE SOCIAL') 
print('========================================\n')

print('1 - Inserir arquivo de teste')
print('2 - Sair \n')

opcao_inicial = int(input('Digite a opção: \n'))

match opcao_inicial:
    case 1:
        arquivo = input('Digite o nome do arquivo de teste (exemplo: grafo_1.txt): \n')
        resultado = leitura_arquivo(arquivo)

        if resultado:
            vertices, arestas, matriz = resultado

            grafo = Grafo(vertices=vertices, arestas=arestas, matriz=matriz)
        
            print('Grafo carregado com sucesso!')

        else:
            sys.exit()

    case 2:
        print('Saindo...')
        sys.exit()

while True:
    print('\n')
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
    print('0 - Sair\n')

    opcao_grafo = opcao_inicial = int(input('Digite a opção: '))

    match opcao_grafo:
        case 0:
            print('Saindo...')
            break

        case 1:
            print(f'Ordem do grafo: {grafo.ordem()}')

        case 2:
            print(f'Tamanho do grafo: {grafo.tamanho()}')

        case 3:
            print(f'Densidade do grafo: {grafo.densidade()}')

        case 4:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber seus vizinhos: '))
            validar_vertice(vertice, grafo.ordem())

            print(f'Vizinhos do vértice {vertice}: {grafo.vizinhos(vertice)}')

        case 5:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber seu grau: '))
            validar_vertice(vertice, grafo.ordem())
            
            print(grafo.grau_vertice(vertice))

        case 6:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para saber se ele é ou não articulação: '))
            validar_vertice(vertice, grafo.ordem())

            eh_articulacao = grafo.vertice_eh_articulacao(vertice)
            print('O vértice é articulação!' if eh_articulacao else 'O vértice não é articulação')

        case 7:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice origem: '))
            validar_vertice(vertice, grafo.ordem())

            sequencia_visitados, arestas_retorno = grafo.busca_largura(vertice)

            print(f'Sequência de vértices visitados: {sequencia_visitados}')
            print(f'Arestas de retorno (não fazem parte da árvore de busca): {arestas_retorno}')

        case 8:
            grafo.componentes_conexas()

        case 9:
            ciclo = grafo.possui_ciclo()

            print('Sim, grafo possui ciclo' if ciclo else 'Não, grafo não possui ciclo.')

        case 10:
            vertice = int(input(f'Escolha um vértice de 1 até {grafo.ordem()} para ser o vértice origem: '))
            validar_vertice(vertice, grafo.ordem())

            lista_caminhos = grafo.caminhos_minimos(vertice)

            print(f'Caminhos mínimos: {lista_caminhos}')

        case _:
            print('Opção inválida!')