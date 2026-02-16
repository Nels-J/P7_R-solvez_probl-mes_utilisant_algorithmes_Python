from typing import Dict


def display_result(result: Dict) -> None:
    print(f"Tested combinations: {result['dp_iterations']}")
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
