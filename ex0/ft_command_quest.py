#!/usr/bin/env python3
import sys

input_user = len(sys.argv)
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Arguments received: {input_user}")
else:
    print("No argument provided!")
print(f"Total arguments: {input_user}")
