import networkx as nx
import matplotlib.pyplot as plt

def ler_tabela(arquivo):
    tabela = []
    with open(arquivo, 'r') as file:
        next(file)  # Ignorar a primeira linha
        for line in file:
            row = line.split()
            tabela.append(row)
    return tabela

def plotar_grafo(tabela):
    G = nx.Graph()
    num_vertices = len(tabela)

    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if tabela[i][j] != '-' and tabela[i][j].isdigit():
                peso = int(tabela[i][j])
                G.add_edge(chr(65+i), chr(65+j), weight=peso)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo")
    plt.show()

def plotar_subgrafo_conexo_minimo(tabela):
    G = nx.Graph()
    num_vertices = len(tabela)

    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if tabela[i][j] != '-' and tabela[i][j].isdigit():
                peso = int(tabela[i][j])
                G.add_edge(chr(65+i), chr(65+j), weight=peso)

    mst = nx.minimum_spanning_tree(G)
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Subgrafo Gerador Conexo de Peso Mínimo")
    plt.show()

def plotar_subgrafo_completo_minimo(tabela):
    G = nx.Graph()
    num_vertices = len(tabela)

    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if tabela[i][j] != '-' and tabela[i][j].isdigit():
                peso = int(tabela[i][j])
                G.add_edge(chr(65+i), chr(65+j), weight=peso)

    complete_graph = nx.complete_graph(G)
    mst_complete = nx.minimum_spanning_tree(complete_graph)
    pos = nx.spring_layout(complete_graph)
    labels = nx.get_edge_attributes(complete_graph, 'weight')

    nx.draw(complete_graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
    nx.draw_networkx_edge_labels(complete_graph, pos, edge_labels=labels)
    plt.title("Subgrafo Gerador Completo de Peso Mínimo")
    plt.show()

# Ler a tabela do arquivo
arquivo = ('grafo.txt')
tabela = ler_tabela(arquivo)

# Plotar o grafo original
plotar_grafo(tabela)

# Plotar o subgrafo gerador conexo de peso mínimo
plotar_subgrafo_conexo_minimo(tabela)

# Plotar o subgrafo gerador completo de peso mínimo
plotar_subgrafo_completo_minimo(tabela)
