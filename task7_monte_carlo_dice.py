import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(n_simulations=100000):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(n_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    probabilities = {s: (count / n_simulations) for s, count in sum_counts.items()}
    return probabilities

def analytical_probabilities():
    total_outcomes = 36
    return {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

def plot_probabilities(mc_probs, analytical_probs):
    labels = list(range(2, 13))
    mc_values = [mc_probs[k] for k in labels]
    analytical_values = [analytical_probs[k] for k in labels]

    x = range(len(labels))
    plt.figure(figsize=(10, 5))
    plt.bar(x, mc_values, width=0.4, label='Монте-Карло', align='center')
    plt.bar([i + 0.4 for i in x], analytical_values, width=0.4, label='Аналітичні', align='center')
    plt.xticks([i + 0.2 for i in x], labels)
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Приклад запуску:
# mc = monte_carlo_simulation()
# analytical = analytical_probabilities()
# plot_probabilities(mc, analytical)