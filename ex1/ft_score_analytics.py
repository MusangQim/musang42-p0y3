#!/usr/bin/env python3
import sys


def main() -> None:
    user_input = len(sys.argv)
    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if user_input > 1 and scores:
        print(f"Scores processed: {scores}")
        total_player = len(scores)
        print(f"Total players: {total_player}")
        total_score = sum(scores)
        print(f"Total score: {total_score}")
        average_score = (total_score / total_player)
        print(f"Average score: {average_score:.1f}")
        high_score = max(scores)
        print(f"High score: {high_score}")
        low_score = min(scores)
        print(f"Low score: {low_score}")
        score_range = high_score - low_score
        print(f"Score range: {score_range}")
    else:
        print("No scores provided. Usage:",
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
