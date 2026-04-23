#!/usr/bin/env python3
import random


def main() -> None:
    # --- using List Comprehensive ---
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
             'Gregory', 'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {names}")
    all_capital = [players.capitalize() for players in names]
    print(f"New list with all capitalized: {all_capital}")
    only_capital = [player for player in names
                    if player == player.capitalize()]
    # or it can use:
    # only_capital = [player for player in names if player.istitle()]
    print(f"New list of capitalized names only: {only_capital}")
    print()
    # --- using Dictionary Comprehensive ---
    scores = {name: random.randint(1, 1000) for name in all_capital}
    print(f"Score dict: {scores}")
    score_average = sum(scores.values()) / len(scores)
    print(f"Score average is {score_average:.2f}")
    score_high = {name: score for name, score in scores.items()
                  if score > score_average}
    print(f"High scores: {score_high}")


if __name__ == "__main__":
    main()
