# TP1-Grafos
Primeiro trabalho de grafos.


## Arquivo utils

**def leitura_arquivo(nome_arquivo)**

A função recebe como entrada o nome do arquivo `.txt` que contém os dados do grafo e, a partir dessas informações, constrói e retorna sua matriz de adjacência, sua ordem (quantidade de vértices) e seu tamanho (quantidade de arestas).

```py
quantidade_vertices, quantidade_arestas, matriz = utils.leitura_arquivo("grafoteste.txt")
```