#!/usr/bin/env python3
import sys

# Function definition for fizzbuzz
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Call the fizzbuzz function
fizzbuzz()
print("")  # Print a new line after fizzbuzz execution

# Access command-line arguments
args = sys.argv[1:]
print("Command-line arguments:", args)

