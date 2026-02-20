# Student Project: Investment Solver 
---
# Quick Usage

## English

This project contains two scripts: `bruteforce.py` and `optimized.py`.

### Usage
- Run the brute-force solver:

>>Exhaustive search — enumerate all subsets of actions, test total cost ≤ budget and keep the subset with maximum profit.

```bash
  python3 bruteforce.py
```

- Run the dynamic programming (optimized) solver:

>>Dynamic programming 0/1 knapsack — build a DP table over items and budget states to compute the maximal profit and reconstruct chosen items.

```bash
  python3 optimized.py
```

### Input data formats
- `bruteforce.py` (expects `Actions_list.csv` by default):
  - CSV headers (French): `Actions #`, `Coût par action (en euros)`, `Bénéfice (après 2 ans)`
  - Example row: `Action-1`, `20`, `5%`
  - Notes: costs are in euros (commas allowed as decimal separators), benefit is a percentage (with `%`).

- `optimized.py` (uses `toolbox.data_tools.load_actions` — default datasets `dataset1_Python_P7.csv`, `dataset2_Python_P7.csv`):
  - CSV headers: `name`, `price`, `profit`
  - Example row: `Share-FOO`, `15.06`, `5.91`
  - Notes: `price` is in euros (float), `profit` is a percentage (e.g. `5.91` means 5.91%). The script converts prices to centimes internally.

### Default behavior
- Both scripts assume a maximum budget of 500 €.

---

## Français

Ce dépôt contient deux scripts : `bruteforce.py` et `optimized.py`.

### Utilisation
- Lancer le solver par force brute :

>> Recherche exhaustive — énumère toutes les combinaisons d'actions, filtre celles sous budget et choisit celle donnant le maximum de profit.

```bash
  python3 bruteforce.py
```

- Lancer le solver optimisé (programmation dynamique) :

>> Programmation dynamique (sac à dos 0/1) — calcule la meilleure valeur pour chaque état (items × budget) et reconstruit la sélection optimale.

```bash
  python3 optimized.py
```

### Format des données d'entrée
- `bruteforce.py` (attend `Actions_list.csv` par défaut) :
  - En-têtes CSV (français) : `Actions #`, `Coût par action (en euros)`, `Bénéfice (après 2 ans)`
  - Exemple : `Action-1`, `20`, `5%`
  - Remarques : les coûts sont en euros (les virgules décimales sont acceptées), le bénéfice est un pourcentage (avec `%`).

- `optimized.py` (utilise `toolbox.data_tools.load_actions` — jeux `dataset1_Python_P7.csv`, `dataset2_Python_P7.csv`) :
  - En-têtes CSV : `name`, `price`, `profit`
  - Exemple : `Share-FOO`, `15.06`, `5.91`
  - Remarques : `price` est en euros (float), `profit` est un pourcentage (ex. `5.91` signifie 5.91%). Le script convertit les prix en centimes pour le calcul.

### Comportement par défaut
- Les deux scripts utilisent un budget maximum de 500 €.

---