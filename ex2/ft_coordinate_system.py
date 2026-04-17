#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        coords_input = input("Enter new coordinates "
                             "as floats in format 'x,y,z': ")
        coords_split = coords_input.split(",")
        if len(coords_split) != 3:
            print("Invalid syntax")
        else:
            # for part in coords_split:
            try:
                x = float(coords_split[0])
            except ValueError as e:
                print(f"Error on parameter '{coords_split[0]}': {e}")
                continue
            try:
                y = float(coords_split[1])
            except ValueError as e:
                print(f"Error on parameter '{coords_split[1]}': {e}")
                continue
            try:
                z = float(coords_split[2])
            except ValueError as e:
                print(f"Error on parameter '{coords_split[2]}': {e}")
                continue
            return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    x1 = pos1[0]
    y1 = pos1[1]
    z1 = pos1[2]
    distance_formula = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(distance_formula, 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    # print(f"Got a second tuple: {pos2}")
    # print(f"It includes: X={pos2[0]}, Y={pos2[1]}, Z={pos2[2]}")
    x2 = pos2[0]
    y2 = pos2[1]
    z2 = pos2[2]
    distance_formula = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets"
          f" of coordinates: {round(distance_formula, 4)}")


if __name__ == "__main__":
    main()
