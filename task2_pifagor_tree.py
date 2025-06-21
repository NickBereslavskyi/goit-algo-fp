import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth, ax):
    if depth == 0:
        return
    x1 = x + length * np.cos(angle)
    y1 = y + length * np.sin(angle)
    ax.plot([x, x1], [y, y1], color='brown', lw=1)

    draw_tree(x1, y1, angle + np.pi / 4, length * 0.7, depth - 1, ax)
    draw_tree(x1, y1, angle - np.pi / 4, length * 0.7, depth - 1, ax)

def plot_tree(depth):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')
    draw_tree(0, 0, np.pi / 2, 100, depth, ax)
    plt.show()

# Приклад виклику:
# plot_tree(5)