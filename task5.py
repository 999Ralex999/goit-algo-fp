import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)
    return graph


def visualize_traversal(root, traversal_order, title):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    labels = {n: d['label'] for n, d in graph.nodes(data=True)}
    node_ids = [n.id for n in traversal_order]

    colors = []
    for i in range(len(node_ids)):
        ratio = i / (len(node_ids) - 1) if len(node_ids) > 1 else 1
        
        color = f"#{int(18 + (255 - 18) * ratio):02X}{int(150 + (255 - 150) * ratio):02X}F0"
        colors.append((node_ids[i], color))

    node_colors = []
    for node in graph.nodes:
        found = next((c for i, c in colors if i == node), '#E0E0E0')
        node_colors.append(found)

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, labels=labels, node_color=node_colors, node_size=2500, arrows=False)
    plt.title(title)
    plt.show()


def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited


def bfs(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited


if __name__ == "__main__":
   
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")

    # DFS
    dfs_order = dfs(root)
    visualize_traversal(root, dfs_order, "Обхід в глибину (DFS)")

    # BFS
    bfs_order = bfs(root)
    visualize_traversal(root, bfs_order, "Обхід у ширину (BFS)")
