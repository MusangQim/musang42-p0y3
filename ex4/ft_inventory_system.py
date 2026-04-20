#!/usr/bin/env python3
import sys

inventory = {}


def main():
    for arg in sys.argv[1:]:
        input_user = arg.split(':')
        if len(input_user) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if input_user[0] in inventory:
            print(f"Redundant item '{input_user[0]}' - discarding")
            continue
        try:
            convert = int(input_user[1])
            inventory[input_user[0]] = convert
        except ValueError as e:
            print(f"Quantity error for '{input_user[0]}': {e}")
    check_keys = inventory.keys()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(check_keys)}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(check_keys)} items: {total}")
    for key, value in inventory.items():
        print(key, value)

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
