from dataclasses import dataclass
from typing import List
import csv
import itertools
import time

MAX_BUDGET_EUR = 500  # Maximum budget in euros for investment


@dataclass
class Action:
    """Dataclass to hold information about an action."""
    name: str
    cost: float
    profit_rate: float  # decimal, e.g. 0.10 for 10%


@dataclass
class InvestmentResult:
    """Dataclass to hold the result of the best investment found."""
    actions: List[Action]
    total_cost: float
    total_profit: float
    tested_combinations: int  # Number of combinations tested
    elapsed_seconds: float  # Time taken to compute the result
    initial_actions_count: int  # number of actions in the initial panel


def load_actions(csv_file: str) -> List[Action]:
    """
    Load actions from a CSV file with French headers and return list of Action.
    :param csv_file: Path to the CSV file
    :return: List of Action dataclass instances
    """
    available_actions: List[Action] = []

    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Actions #"].strip()
            cost_str = row["Coût par action (en euros)"].strip().replace(",", ".")
            benefit_str = row["Bénéfice (après 2 ans)"].strip().replace("%", "").replace(",", ".")
            cost = float(cost_str)  # in euros
            profit_rate = float(benefit_str) / 100.0  # Convert percentage to decimal
            available_actions.append(Action(name=name, cost=cost, profit_rate=profit_rate))

    return available_actions


def calculate_profit(actions: List[Action]) -> float:
    """
    Calculate total profit after 2 years for a list of Action.
    :param actions: List of Action
    :return: Total profit as float
    """
    return sum(action.cost * action.profit_rate for action in actions)


def calculate_cost(actions: List[Action]) -> float:
    """
    Calculate total investment cost for a list of Action.
    :param actions: List of Action
    :return: Total cost as float
    """
    return sum(action.cost for action in actions)


def brute_force_best_investment(actions: List[Action]) -> InvestmentResult:
    """
    Explore all possible combinations to find the best investment.
    :param actions: List of available actions
    :return: Best investment result as InvestmentResult dataclass instance
    """
    start_time = time.perf_counter()
    initial_count = len(actions)

    best_profit = 0.0
    best_combination: List[Action] = []
    tested_combinations = 0

    for r in range(1, initial_count + 1):
        for combo in itertools.combinations(actions, r):
            tested_combinations += 1
            total_cost = calculate_cost(list(combo))
            if total_cost <= MAX_BUDGET_EUR:
                total_profit = calculate_profit(list(combo))
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = list(combo)

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    return InvestmentResult(
            actions=best_combination,
            total_cost=calculate_cost(best_combination),
            total_profit=best_profit,
            tested_combinations=tested_combinations,
            elapsed_seconds=elapsed,
            initial_actions_count=initial_count,
    )


def display_result(result: InvestmentResult) -> None:
    """
    Print the result of the best investment found.
    """
    # Format elapsed time
    hours, remainder = divmod(result.elapsed_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    formatted_time = (
            f"{int(hours):02d}:"
            f"{int(minutes):02d}:"
            f"{int(seconds):02d}."
            f"{int(milliseconds):03d}"
    )
    # Format and print results
    print("Best investment found - Brute Force Approach")
    print(f"Initial actions in panel: {result.initial_actions_count}")
    print(f"Tested combinations: {result.tested_combinations}")
    print(f"Execution time: {formatted_time}")
    print("-" * 20)
    print(f"Total cost: {result.total_cost:.2f} €")
    print(f"Total profit after 2 years: {result.total_profit:.2f} €")
    selected_count = len(result.actions)
    label = "action" if selected_count == 1 else "actions"
    print(f"\nList of selected action(s) — {selected_count} {label}:")
    for action in result.actions:
        profit = action.cost * action.profit_rate
        print(f"- {action.name} — {action.cost:.2f} € (Profit: {profit:.2f} €)")


if __name__ == "__main__":
    actions = load_actions("Actions_list.csv")
    best_investment = brute_force_best_investment(actions)
    display_result(best_investment)
