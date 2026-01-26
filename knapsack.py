# https://www.youtube.com/watch?v=qxWu-SeAqe4
# Other solution : https://github.com/ByteQuest0/Implemention_codes/blob/main/Dynamic%20Programming/knapsack.py

import time

actions = [
        {
                'name'  : 'item1',
                'cost'  : 3,
                'profit': 50,
        },
        {
                'name'  : 'item2',
                'cost'  : 2,
                'profit': 40,
        },
        {
                'name'  : 'item3',
                'cost'  : 4,
                'profit': 70,
        },
        {
                'name'  : 'item4',
                'cost'  : 5,
                'profit': 80,
        },
        {
                'name'  : 'item5',
                'cost'  : 1,
                'profit': 10,
        }
]

capacity = 7


def best_investment_dp(actions, capacity):
    """
    Find the best investment using a Dynamic Programming approach to solve the 0/1 knapsack problem.
    :param actions: List of available actions
    :return: Best investment result dictionary
    """
    start_time = time.perf_counter()
    #
    # # Convert to integer weights (centimes) to use DP array indices
    # budget_cents = int(capacity * 100)
    # weights = [int(round(a["cost"] * 100)) for a in actions]
    weights = [a['cost'] for a in actions]
    values = [a["profit"] for a in actions]

    numbers_of_actions = len(actions)
    dp = [0.0] * (capacity + 1)
    item_index = [-1] * (capacity + 1)  # index of last item used to reach capacity c
    prev = [-1] * (capacity + 1)        # previous capacity before adding that item

    iterations = 0
    for i in range(numbers_of_actions):
        w = weights[i]
        v = values[i]
        if w > capacity:
            continue
        # parcours inverse pour 0/1 knapsack
        for c in range(capacity, w - 1, -1):
            iterations += 1
            newv = dp[c - w] + v
            if newv > dp[c]:
                dp[c] = newv
                item_index[c] = i
                prev[c] = c - w

    # trouver la capacité maximale atteinte
    best_capacity = max(range(capacity + 1), key=lambda c: dp[c])
    best_profit = dp[best_capacity]

    # reconstruire la solution
    selected_indices = []
    c = best_capacity
    visited = set()
    while c > 0 and item_index[c] != -1:
        i = item_index[c]
        if i in visited:
            break  # sécurité
        selected_indices.append(i)
        visited.add(i)
        c = prev[c]

    selected_indices.reverse()
    best_combination = [actions[i] for i in selected_indices]

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    formatted_time = (
        f"{int(hours):02d}:"
        f"{int(minutes):02d}:"
        f"{int(seconds):02d}."
        f"{int(milliseconds):03d}"
    )
    print(f"⏱ DP algorithm execution time : {formatted_time}")

    return {
        "actions": best_combination,
        "total_cost": sum(a["cost"] for a in best_combination),
        "total_profit": best_profit,
        "tested_combinations": iterations,
    }


# --- example ---
if __name__ == "__main__":
    print(best_investment_dp(actions, capacity))


