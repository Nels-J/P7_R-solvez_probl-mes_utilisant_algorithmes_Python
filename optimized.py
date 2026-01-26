import time
from typing import List, Dict

from cli_display import display_result
from data_tools import load_actions

MAX_BUDGET_EUROS = 500 # Maximum budget in euros for investment
CAPACITY_CENTS = MAX_BUDGET_EUROS * 100 # Capacity changed to centimes for integer calculations

def clean_actions(actions: List[Dict]) -> List[Dict]:
    """
    Remove actions with non-positive cost or benefit.
        IF cost <= 0 or benefit <= 0 then the action is invalid.
    :param actions: List of actions
    :return: Filtered list of actions
    """
    cleaned_actions = []
    for action in actions:
        if action["cost"] <= 0 or action["benefit"] <= 0:
            continue

        cleaned_actions.append({
                'name': action["name"],
                'cost': int(action["cost"] * 100), # Convert cost to centimes
                'profit': int(action["cost"] * action["benefit"]), # Calculate profit in centimes
        })
    return cleaned_actions

def best_investment_dp(actions, capacity ):
    """
    Find the best investment using a Dynamic Programming approach to solve the 0/1 knapsack problem.
    :param actions: List of available actions
    :return: Best investment result dictionary
    """
    start_time = time.perf_counter()

    weights = [a['cost'] for a in actions]
    values = [a["profit"] for a in actions]
    # print(weights , values) # debug to removed

    numbers_of_actions = len(actions)
    dp = [0] * (capacity + 1)
    item_index = [-1] * (capacity + 1)  # index of last item used to reach capacity c
    prev = [-1] * (capacity + 1)        # previous capacity before adding that item

    iterations = 0
    for i in range(numbers_of_actions):
        w = weights[i]
        v = values[i]
        if w > capacity:
            continue

        # 0/1 knapsack DP update (in reverse to avoid reuse of the same item)
        for c in range(capacity, w - 1, -1):
            iterations += 1
            newv = dp[c - w] + v
            if newv > dp[c]:
                dp[c] = newv
                item_index[c] = i
                prev[c] = c - w

    # find the best profit and corresponding capacity
    best_capacity = max(range(capacity + 1), key=lambda c: dp[c])
    best_profit = dp[best_capacity]

    # reconstruct the best combination of actions
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
        "dp_iterations": iterations,
    }

if __name__ == "__main__":
    dataset1_loaded = load_actions("dataset1_Python_P7.csv") # Smaller dataset
    actions1 = clean_actions(dataset1_loaded)
    optimized_investment1 = best_investment_dp(
            actions1,
            CAPACITY_CENTS
    )
    display_result(optimized_investment1)
    # print(optimized_investment1) # debug to remove

    dataset2_loaded = load_actions("dataset2_Python_P7.csv")  # Larger dataset
    actions2 = clean_actions(dataset2_loaded)
    optimized_investment2 = best_investment_dp(
            actions2,
            CAPACITY_CENTS
    )
    display_result(optimized_investment2)
    # print(optimized_investment2) # debug to remove




