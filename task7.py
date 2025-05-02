import random
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(trials=100000):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(trials):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] += 1

    probabilities = {k: v / trials for k, v in results.items()}
    return probabilities


def analytical_probabilities():
    
    distribution = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5,
        7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    total = 36
    return {k: v / total for k, v in distribution.items()}


def plot_probabilities(mc_probs, analytical_probs):
    sums = list(range(2, 13))
    mc = [mc_probs[s] for s in sums]
    analytical = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    plt.bar([x - bar_width / 2 for x in sums], mc, width=bar_width, label="Монте-Карло", color="#4CAF50")
    plt.bar([x + bar_width / 2 for x in sums], analytical, width=bar_width, label="Аналітичні", color="#2196F3")

    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Порівняння ймовірностей сум кубиків")
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    trials = 100000
    mc_probs = monte_carlo_dice_simulation(trials)
    analytical_probs = analytical_probabilities()

    print("=== Ймовірності Монте-Карло ===")
    for s in sorted(mc_probs):
        print(f"Сума {s}: {mc_probs[s]:.4f}")

    print("\n=== Аналітичні ймовірності ===")
    for s in sorted(analytical_probs):
        print(f"Сума {s}: {analytical_probs[s]:.4f}")

    plot_probabilities(mc_probs, analytical_probs)
