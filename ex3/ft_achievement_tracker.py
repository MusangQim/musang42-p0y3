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
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    # --- Set Union ---
    player_union = alice.union(bob).union(charlie).union(dylan)
    print(f"All distinct achievements: {player_union}\n")
    # --- Set Intersection ---
    player_intersec = alice.intersection(bob) \
                           .intersection(charlie) \
                           .intersection(dylan)
    print(f"Common achievements: {player_intersec}\n")
    # --- Set Difference ---
    alice_diff = alice.difference(bob).difference(charlie).difference(dylan)
    bob_diff = bob.difference(alice).difference(charlie).difference(dylan)
    charlie_diff = charlie.difference(alice).difference(bob).difference(dylan)
    dylan_diff = dylan.difference(alice).difference(bob).difference(charlie)
    print(f"Only Alice has: {alice_diff}")
    print(f"Only Bob has: {bob_diff}")
    print(f"Only Charlie has: {charlie_diff}")
    print(f"Only Dylan has: {dylan_diff}")


if __name__ == "__main__":
    main()
