#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10  # Calculate the last digit using absolute value
print(f"The last digit of {number} is {last}{' and is greater than 5' if last > 5 else (' and is 0' if last == 0 else ' and is less than 6 and not 0')}")


