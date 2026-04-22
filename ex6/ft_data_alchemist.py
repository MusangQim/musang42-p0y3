#!/usr/bin/env python3

import random


def main() -> None:
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===\n")
    all_capitalize = [players.capitalize() for players in names]
    print(all_capitalize)


if __name__ == "__main__":
    main()
