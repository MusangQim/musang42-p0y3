#!/usr/bin/env python3
import sys

user_input = len(sys.argv)
print("=== Player Score Analytics ===")
scores = []
for arg in sys.argv[1:]:
    try:
        score = int(arg)
        scores.append(score)
        print(f"Scores processed: {scores}")
    except ValueError as e:
        print(f"Invalid parameter: {e}")
        exit
#print(f"Scores processed: {scores}")
if user_input > 1:
    total_player = user_input - 1
    print(f"Total players: {total_player}")
else:
    print("No score provided.")
