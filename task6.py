def greedy_algorithm(items, budget):
   
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected = {}
    total_cost = 0
    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected[name] = info
            total_cost += info['cost']
    return selected


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    res = {}
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            res[name] = items[name]
            w -= items[name]['cost']

    return res


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("=== Жадібний алгоритм ===")
    for name in greedy_result:
        print(f"{name}: {greedy_result[name]}")

    print("\n=== Динамічне програмування ===")
    for name in dp_result:
        print(f"{name}: {dp_result[name]}")
