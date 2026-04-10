#!/usr/bin/env python3
import sys

input_user = len(sys.argv)
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) > 1:
    input_receive = input_user - 1
    print(f"Arguments received: {input_receive}")
    for input_list in range(1, len(sys.argv)):
        print(f"Argument {input_list} : {sys.argv[input_list]}")
else:
    print("No argument provided!")
print(f"Total arguments: {input_user}")
