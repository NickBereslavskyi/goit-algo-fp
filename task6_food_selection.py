def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій/вартість у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected.append(name)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data['cost']
        calories = data['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних предметів
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, data = item_list[i - 1]
            selected.append(name)
            w -= data['cost']

    selected.reverse()
    total_cost = sum(items[name]['cost'] for name in selected)
    total_calories = sum(items[name]['calories'] for name in selected)

    return selected, total_cost, total_calories


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# greedy_result = greedy_algorithm(items, budget)
# dp_result = dynamic_programming(items, budget)

# print("Greedy:", greedy_result)
# print("Dynamic Programming:", dp_result)