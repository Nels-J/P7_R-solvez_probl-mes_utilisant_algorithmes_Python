from typing import Dict


def display_result(result: Dict) -> None:
    print(f"Tested combinations: {result['tested_combinations']}")
    print("-" * 60)
    print("Best investment found")
    print("-" * 60)
    print(f"Total cost: {result['total_cost']:.2f} €")
    print(f"Total profit after 2 years: {result['total_profit']:.2f} €")

    print("\nSelected actions:")
    for action in result["actions"]:
        print(f"- {action['name']} {action['cost']} € (Profit: {action['cost'] * action['benefit']:.2f} €)")
