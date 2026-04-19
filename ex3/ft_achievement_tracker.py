#!/usr/bin/env python3
import random

achievements = [
    "Crafting Genuis",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer"
]

def gen_player_achievements() -> set:
    count = random.randint(3, 8)
    picks = random.sample(achievements, count)
    return set(picks)

def main() -> None:
    alice = gen


if __name__ == "__main__":
    main()
