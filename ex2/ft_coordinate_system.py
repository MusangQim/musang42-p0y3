#!/usr/bin/env python3
import math

def get_player_pos():
    coords_input = input(float("Enter new coordinates as floats in format: 'x,y,z':"))
    coords_split = coords_input.split(",")
    if len(coords_split) != 3:
        print("Invalid syntax")
    else:


def main():
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    get_player_pos()


if __name__ == "__main__":
    main()
