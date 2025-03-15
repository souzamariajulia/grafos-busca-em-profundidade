import networkx as nx
import matplotlib.pyplot as plt

arquivo = "./G2.txt"
fig, ax = plt.subplots()

def plotar(vertices, arestas, cores):

    ax.clear()

    GRAFO = nx.DiGraph()
    GRAFO.add_nodes_from(vertices)
    GRAFO.add_edges_from(arestas)

    posicoes = nx.circular_layout(GRAFO)
    nx.draw(GRAFO, posicoes, with_labels =True, font_weight="bold", node_size=700, font_size= 20, font_color="white", arrowsize=15)
    
    for i in cores:
        if cores[i] == "cinza":
            cor = "gray"
        elif cores[i] == "preto":
            cor = "black"
        else:
            cor = "white"
        nx.draw_networkx_nodes(
            GRAFO,
            pos=posicoes,
            nodelist=[i],
            node_color=cor,
            cmap=plt.cm.Blues,
            node_size=800,  # Ajuste o tamanho conforme necessário
        )

    plt.show(block=False)
    plt.pause(1.5)
    plt.close()

#função que recebe um grafo como parametro 
def DFS(grafo):
    global cor, d, f, tipo_aresta, vm #inicializando váriaveis globais 
    cor, d, f, tipo_aresta, vm = {}, {}, {}, [], 0
    
    vertices = sorted(grafo, key=lambda v: len(grafo[v]), reverse=True)

    for u in vertices:
        if cor.get(u, 'branco') == 'branco':
            DFS_VISIT(grafo, u)
#função que recebe o grafo e um vertice como parametro 
def DFS_VISIT(grafo, u):
    global cor, d, f, tipo_aresta, vm
    cor[u] = 'cinza'
    vm += 1
    d[u] = vm

#se o vertice igual a branco chamar a função visit e usando o append para inserir no final da lista
    plotar(vertices_arquivo, arestas_arquivo, cor) # ICARO 
    for v in grafo[u]:
        if cor.get(v, 'branco') == 'branco':
            tipo_aresta.append(f"Aresta ({u}, {v}): Árvore")
            DFS_VISIT(grafo, v)
        elif d[u] < d.get(v, 0):
            tipo_aresta.append(f"Aresta ({u}, {v}): Avanço")
        elif cor[v] == 'cinza':
            tipo_aresta.append(f"Aresta ({u}, {v}): Retorno")
        else:
            tipo_aresta.append(f"Aresta ({u}, {v}): Cruzamento")
    cor[u] = 'preto'
    plotar(vertices_arquivo, arestas_arquivo, cor) #ICARO
    vm += 1
    f[u] = vm

def ler_grafo_do_arquivo(arq): #função para a leitura do arquivo que contém o grafo
    vertices = set()
    arestas = []
    grafo = {}

    with open(arq, 'r') as arquivo:
        info = arquivo.readline().split()  #lê a primeira linha que contém as informações sobre o grafo(vertices, arestas
        # e se é grafo ou digrafo)

        if len(info) < 3:   #verifica se tem as três informações sobre o grafo
            print("Formato inválido da primeira linha.")
            return vertices, arestas

        num_vertices, num_arestas, tipo_grafo = int(info[0]), int(info[1]), info[2]

        for _ in range(num_arestas): #leitura das arestas 
            linha = arquivo.readline().split()

            if len(linha) >= 2: #verfica se tem pelo menos dois elementos que são os vértices
                try:
                    u, v = int(linha[0]), int(linha[1])  #converte para inteiros
                except Exception:
                    u, v = (linha[0], linha[1])
                vertices.add(u) #adiciona vértices à lista
                vertices.add(v)

                #CRIAR LISTA DE ADJ
                if u not in grafo:
                    grafo[u] = []

                arestas.append((u, v)) #adciona a aresta que liga esses dois vértices à lista
                grafo[u].append(v)
            else:
                print("Formato inválido em uma linha de aresta. Ignorando.")

    return list(vertices), arestas, grafo

vertices_arquivo, arestas_arquivo, grafo = ler_grafo_do_arquivo(arquivo)

DFS(grafo)

print("Valores do vetor d:", d)
print("Valores do vetor f:", f)
print("Nomenclatura das arestas:")
for aresta in tipo_aresta:
    print(aresta)