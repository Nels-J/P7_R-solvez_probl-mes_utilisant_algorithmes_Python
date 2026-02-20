import time
from typing import List, Dict, Tuple

from toolbox.cli_display import display_optimized_result
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

        cost_cents = int(round(action["cost"] * 100))  # Convert cost to centimes
        # 'benefit' in the CSV is a percentage (e.g. 12.5 for 12.5%),
        # so profit in cents is cost_cents * (benefit / 100).
        profit_cents = int(round(cost_cents * (action["benefit"] / 100.0)))

        cleaned_actions.append(
                {
                        "name"  : action["name"],
                        "cost"  : cost_cents,
                        "profit": profit_cents,
                },
        )
    return cleaned_actions


def best_investment_dp(items, budget) -> Tuple[int, List[dict], float, int]:
    """
    Find the best investment using a Dynamic Programming approach to solve the 0/1 knapsack problem.
    Returns a tuple: (best_profit_cents, chosen_items, elapsed_seconds, dp_iterations)
    :param items: List of available actions (with 'cost' and 'profit' in cents)
    :param budget: Budget in cents
    :return: (max profit in cents, list of chosen items, elapsed seconds, dp iterations)
    """
    start_time = time.perf_counter()

    n = len(items)
    if budget < 0:
        raise ValueError("budget must be > 0")

    # dp[i][b] = max profit using first i items within budget b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]  # reconstruction

    dp_iterations = 0
    for i in range(1, n + 1):
        it = items[i - 1]
        for b in range(budget + 1):  # for each budget from 0 to max budget
            # count this decision (state evaluation)
            dp_iterations += 1

            # option 1: don't take
            best = dp[i - 1][b]
            chosen = False

            # option 2: take (if fits)
            if it["cost"] <= b:
                candidate = dp[i - 1][b - it["cost"]] + it["profit"]
                if candidate > best:
                    best = candidate
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

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    return dp[n][budget], chosen_items, elapsed, dp_iterations


if __name__ == "__main__":
    dataset1_loaded = load_actions("dataset1_Python_P7.csv")
    actions1 = clean_actions(dataset1_loaded)
    best_profit_cents, chosen_items, elapsed, dp_iterations = best_investment_dp(actions1, CAPACITY_CENTS)
    display_optimized_result(best_profit_cents, chosen_items, elapsed, len(actions1), dp_iterations)

    print("\n" + "#" * 80 + "\n" )

    dataset2_loaded = load_actions("dataset2_Python_P7.csv")
    actions2 = clean_actions(dataset2_loaded)
    best_profit_cents, chosen_items, elapsed, dp_iterations = best_investment_dp(actions2, CAPACITY_CENTS)
    display_optimized_result(best_profit_cents, chosen_items, elapsed, len(actions2), dp_iterations)