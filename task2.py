import matplotlib.pyplot as plt
import numpy as np
import math

def draw_pythagoras_tree(x, y, length, angle, level):
    """
    Рекурсивна функція для побудови дерева Піфагора
    """
    if level == 0:
        return

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)

    plt.plot([x, x2], [y, y2], color="green", linewidth=1.5)

    new_length = length * 0.7
    draw_pythagoras_tree(x2, y2, new_length, angle + math.pi / 4, level - 1)
    draw_pythagoras_tree(x2, y2, new_length, angle - math.pi / 4, level - 1)

if __name__ == "__main__":

    try:
        depth = int(input("Введіть рівень рекурсії (1-15): "))
        if depth < 1 or depth > 15:
            raise ValueError
    except ValueError:
        print("Невірне значення. Застосовано рівень 10.")
        depth = 10

    plt.figure(figsize=(10, 8))
    plt.axis("off")
    plt.title(f"Фрактал Дерево Піфагора (r={depth})")

    draw_pythagoras_tree(x=0, y=0, length=100, angle=math.pi / 2, level=depth)

    plt.show()
