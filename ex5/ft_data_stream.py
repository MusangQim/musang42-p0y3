#!/usr/bin/env python3
import random
import typing

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "swim", "move"]


def gen_event() -> typing.Generator:
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)


def consume_event(event_list: list) -> typing.Generator:
    while event_list:
        random_event = random.choice(event_list)
        index = event_list.index(random_event)
        event_list.pop(index)
        yield random_event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        name, action = event
        print(f"Event {i}: Player {name} did action {action}")
    event_list = []
    for i in range(10):
        event_list.append(next(event_gen))
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
