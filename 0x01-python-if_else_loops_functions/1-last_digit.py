#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
print(f"Last digit of {number} is", end=" ")
if last == 0:
    print(f"{last} and is 0")
elif last > 5:
    print(f"{last} and is greater than 5")
else:
    print(f"{last} and is less than 6 and is not 0")
