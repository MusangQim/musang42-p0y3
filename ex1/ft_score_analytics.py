#!/usr/bin/env python3
import sys

scores = []
user_input = len(sys.argv)
list_input = str(sys.argv) - 1
print("=== Player Score Analytics ===")
print(f"Score processed: {list_input}")

if user_input > 1:
    total_player = user_input - 1
    print(f"Total players: {total_player}")
else:
    print("No score provided.")
