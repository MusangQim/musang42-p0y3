#!/usr/bin/env python3

import random
import typing

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "swim", "move"]


def gen_event():
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)


# def consume_event() -> None:


def main():
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        name, action = event
        print(f"Event {i}: Player {name} did action {action}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
