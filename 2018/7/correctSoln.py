import networkx as nx

def solve():
    lines = open('d7.in', 'r')
    G = nx.DiGraph()
    for line in lines:
        parts = line.split(" ")
        G.add_edge(parts[1], parts[7])
    print(''.join(nx.lexicographical_topological_sort(G)))

solve()
