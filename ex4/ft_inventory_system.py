#!/usr/bin/env python3
import sys

inventory = {}


def main() -> None:
    print("=== Inventory System Analysis ===")
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
    # --- using dict.keys() ---
    check_keys = inventory.keys()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(check_keys)}")
    # --- using dict.values() ---
    check_value = inventory.values()
    total = sum(check_value)
    print(f"Total quantity of the {len(check_keys)} items: {total}")
    for key, value in inventory.items():
        percentage = round((value / total) * 100, 1)
        print(f"Item {key} represents {percentage}%")
    # --- abundant part ---
    most = max(inventory, key=lambda k: inventory[k])
    print(f"Item most abundant: {most} with quantity {max(check_value)}")
    least = min(inventory, key=lambda k: inventory[k])
    print(f"Item least abundant: {least} with quantity {min(check_value)}")
    # --- using dict.update() ---
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
