from typing import Dict, List


def display_result(result: Dict) -> None:
    print(f"States evaluated: {result['dp_iterations']}")
    print("-" * 50)
    print("Best investment found")
    print("-" * 50)
    print(f"Total cost: {result['total_cost'] / 100:.2f} €")
    print(f"Total profit after 2 years: {result['total_profit'] / 100:.2f} €")

    print("\nSelected action(s):")
    for action in result["actions"]:
        cost_euros = action["cost"] / 100
        profit_euros = action["profit"] / 100

        print(f"- {action['name']} {cost_euros:.2f} € (Profit: {profit_euros:.2f} €)")


def display_optimized_result(best_profit_cents: int, chosen_items: List[Dict], elapsed_seconds: float, valid_actions_count: int, dp_iterations: int = None) -> None:
    """Affiche le résultat produit par best_investment_dp dans un format convivial.

    :param best_profit_cents: profit total en centimes
    :param chosen_items: liste des actions retenues (avec 'cost' et 'profit' en centimes)
    :param elapsed_seconds: temps d'exécution en secondes
    :param valid_actions_count: nombre d'actions valides
    :param dp_iterations: nombre d'itérations / décisions effectuées par l'algorithme DP
    """
    # Formatage du temps
    hours, remainder = divmod(elapsed_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    formatted_time = (
        f"{int(hours):02d}:"
        f"{int(minutes):02d}:"
        f"{int(seconds):02d}."
        f"{int(milliseconds):03d}"
    )

    print("Best investment (DP)")
    print(f"Valid actions from dataset: {valid_actions_count}")
    if dp_iterations is not None:
        print(f"States evaluated: {dp_iterations}")
    print(f"Execution time: {formatted_time}")
    print("-" * 50)
    total_cost_cents = sum(item["cost"] for item in chosen_items)
    print(f"Total cost: {total_cost_cents / 100:.2f} €")
    print(f"Total profit after 2 years: {best_profit_cents / 100:.2f} €")
    selected_count = len(chosen_items)
    label = "action" if selected_count == 1 else "actions"
    print(f"\nList of selected action(s) — {selected_count} {label}:")
    for item in chosen_items:
        profit_eur = item["profit"] / 100
        cost_eur = item["cost"] / 100
        print(f"-> {item['name']} — {cost_eur:.2f} € => Profit: {profit_eur:.2f} €")