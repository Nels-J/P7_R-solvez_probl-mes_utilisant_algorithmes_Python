import csv
import itertools
import time
from typing import List, Dict


MAX_BUDGET = 500 # Maximum budget in euros for investment todo: gérer un choix utilisateur.


def load_actions(csv_file: str) -> List[Dict]: # todo: à déplacer dans un module à part (data_tools?)
    """
    Load actions from a CSV file.

    :param csv_file: Path to the CSV file
    :return: List of actions as dictionaries
    """
    actions = []

    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            actions.append(
                {
                    "name": row["Actions #"],
                    "cost": float(row["Coût par action (en euros)"]),
                    "benefit": float(row["Bénéfice (après 2 ans)"].strip("%")) / 100,
                }
            )

    return actions


def calculate_profit(actions: List[Dict]) -> float:  # todo: a déplacer dans un module à part (financial_tools?)
    """
    Calculate total profit after 2 years.

    :param actions: List of selected actions
    :return: Total profit
    """
    return sum(action["cost"] * action["benefit"] for action in actions)


def calculate_cost(actions: List[Dict]) -> float:  # todo: vers -> financial_tools?
    """
    Calculate total investment cost.

    :param actions: List of selected actions
    :return: Total cost
    """
    return sum(action["cost"] for action in actions)


def brute_force_best_investment(actions: List[Dict]) -> Dict:
    """
    Explore all possible combinations to find the best investment.

    :param actions: List of available actions
    :return: Best investment result
    """
    start_time = time.perf_counter()

    best_profit = 0.0
    best_combination = []
    tested_combinations = 0


    for subset_combination_size in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, subset_combination_size):
            tested_combinations += 1

            total_cost = calculate_cost(combination)

            if total_cost <= MAX_BUDGET:
                total_profit = calculate_profit(combination)

                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    # Format elapsed time
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds - int(seconds)) * 1000

    formatted_time = (
        f"{int(hours):02d}:"
        f"{int(minutes):02d}:"
        f"{int(seconds):02d}."
        f"{int(milliseconds):03d}"
    )

    print(f"⏱ Optimized algorithm execution time : {formatted_time}")

    return {
        "actions": best_combination,
        "total_cost": calculate_cost(best_combination),
        "total_profit": best_profit,
        "tested_combinations": tested_combinations,
    }


def display_result(result: Dict) -> None:
    print("Best investment found")
    print(f"Tested combinations: {result['tested_combinations']}")
    print("-" * 20)
    print(f"Total cost: {result['total_cost']:.2f} €")
    print(f"Total profit after 2 years: {result['total_profit']:.2f} €")

    print("\nSelected actions:")
    for action in result["actions"]:
        print(f"- {action['name']} {action['cost']} € (Profit: {action['cost'] * action['benefit']:.2f} €)")


if __name__ == "__main__":
    actions = load_actions("Actions_list.csv")
    best_investment = brute_force_best_investment(actions)
    display_result(best_investment)
