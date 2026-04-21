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


def consume_event() -> None:


def main():
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        name, action = event
        print(f"Event {i}: Player {name} did action {action}")
    event_list = []
    for i in range(10):
        event_list.append(next(event_gen))
        print(f"Built list of 10 events: {event_list}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
