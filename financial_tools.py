from typing import List, Dict


def calculate_profit(actions: List[Dict]) -> float:
    """
    Calculate total profit after 2 years.

    :param actions: List of selected actions
    :return: Total profit
    """
    return sum(action["cost"] * action["benefit"] for action in actions)


def calculate_cost(actions: List[Dict]) -> float:
    """
    Calculate total investment cost.

    :param actions: List of selected actions
    :return: Total cost
    """
    return sum(action["cost"] for action in actions)
