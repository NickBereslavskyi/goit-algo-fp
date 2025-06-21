import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#B0B0B0"  # Початковий колір
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color_gradient(n, base_color="#1296F0"):
    base_rgb = mcolors.hex2color(base_color)
    hsv = mcolors.rgb_to_hsv(base_rgb)
    gradient = []
    for i in range(n):
        brightness = 0.4 + 0.6 * (i / max(1, n - 1))  # від темного до світлого
        new_rgb = mcolors.hsv_to_rgb((hsv[0], hsv[1], brightness))
        gradient.append(mcolors.to_hex(new_rgb))
    return gradient


def dfs_iterative(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited


def bfs_iterative(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited


def visualize_traversal(root, order="bfs", base_color="#1296F0"):
    if order == "dfs":
        nodes_in_order = dfs_iterative(root)
    else:
        nodes_in_order = bfs_iterative(root)

    colors = generate_color_gradient(len(nodes_in_order), base_color)
    for i, node in enumerate(nodes_in_order):
        node.color = colors[i]

    draw_tree(root)


def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

# Приклад використання:
# tree = build_sample_tree()
# visualize_traversal(tree, order="dfs")
# visualize_traversal(tree, order="bfs")