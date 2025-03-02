
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def dfs_iterative(adj, start):
    visited = [False] * len(adj)
    stack = [start]
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            print(curr, end=" ")
            visited[curr] = True
            for neighbor in reversed(adj[curr]):
                if not visited[neighbor]:
                    stack.append(neighbor)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def visualize_graph(edges, num_nodes):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, font_color="black", edge_color="gray")
    plt.title("Graph Visualization")
    plt.show()

if __name__ == "__main__":
    V = 5
    adj = defaultdict(list)
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 4)
    ]
    for u, v in edges:
        add_edge(adj, u, v)
    print("DFS (iterative) starting from 0:")
    dfs_iterative(adj, 0)
    visualize_graph(edges, V)
