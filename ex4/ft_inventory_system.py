#!/usr/bin/env python3
import sys

inventory = {}
#    "sword" : 1,
#   "shield" : 2,
#    "armor" : 3,
#    "helmet" : 1,
#    "potion" : 1

def main():
    for arg in sys.argv[1:]:
        input_user = arg.split(':')
        if len(input_user) != 2:
            print("Invalid parameter")
            continue
        else:
            print("Redundant item")
            skip
        try:
            convert = int(input_user[1])
        except ValueError:
            print(f"Quantity Error for '{arg}:")

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
