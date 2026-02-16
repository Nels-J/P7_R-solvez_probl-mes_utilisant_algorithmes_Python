from pprint import pprint
from typing import List, Dict

from toolbox.data_tools import load_actions

MAX_BUDGET_EUROS = 500  # Maximum budget in euros for investment
CAPACITY_CENTS = (
        MAX_BUDGET_EUROS * 100
)  # Capacity changed to centimes for integer calculations


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

        cleaned_actions.append(
                {
                        "name"  : action["name"],
                        "cost"  : int(action["cost"] * 100),  # Convert cost to centimes
                        "profit": int(
                                action["cost"] * action["benefit"],
                        ),  # Calculate profit in centimes
                },
        )
    return cleaned_actions


def best_investment_dp(items, budget) -> (int, List[dict]):
    """
    Find the best investment using a Dynamic Programming approach to solve the 0/1 knapsack problem.
    :param actions: List of available actions
    :return:
    """
    n = len(items)
    if budget < 0:
        raise ValueError("budget must be > 0")

    # dp[i][b] = max profit using first i items within budget b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]  # reconstruction

    for i in range(1, n + 1):
        it = items[i - 1]
        for b in range(budget + 1):  # for each budget from 0 to max budget
            # option 1: don't take
            best = dp[i - 1][b]
            chosen = False

            # option 2: take (if fits)
            if it["cost"] <= b:
                cand = dp[i - 1][b - it["cost"]] + it["profit"]
                if cand > best:
                    best = cand
                    chosen = True

            dp[i][b] = best
            take[i][b] = chosen

    # reconstruct chosen items
    chosen_items: List[dict] = []
    b = budget
    for i in range(n, 0, -1):
        if take[i][b]:
            it = items[i - 1]
            chosen_items.append(it)
            b -= it["cost"]

    chosen_items.reverse()
    return (dp[n][budget], chosen_items)


if __name__ == "__main__":
    dataset1_loaded = load_actions("dataset1_Python_P7.csv")  # Smaller dataset
    actions1 = clean_actions(dataset1_loaded)
    optimized_investment1 = best_investment_dp(actions1, CAPACITY_CENTS)

    print(type(optimized_investment1))
    pprint(optimized_investment1)
    print(f"cost: {sum(item['cost'] for item in optimized_investment1[1])} cents")
    print(f"profit: {optimized_investment1[0]} cents")

    dataset2_loaded = load_actions("dataset2_Python_P7.csv")  # Larger dataset
    actions2 = clean_actions(dataset2_loaded)
    optimized_investment2 = best_investment_dp(actions2, CAPACITY_CENTS)
    pprint(optimized_investment2)
    pprint(f"cost: {sum(item['cost'] for item in optimized_investment2[1])} cents")
    pprint(f"profit: {optimized_investment2[0]} cents")
