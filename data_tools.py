import csv
from typing import List, Dict


def load_actions(csv_file: str) -> List[Dict]:
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
                    "name": row["name"],
                    "cost": float(row["price"]),
                    "benefit": float(row["profit"]),
                }
            )

    return actions
