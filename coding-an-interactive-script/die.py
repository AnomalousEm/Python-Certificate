"""
A simple die roller

Author: Emily Shader
Date: December 24,2024
"""

import random

first = int(input("Type the first number: "))
last = int(input("Type the last number: "))

roll = random.randint(first,last)

print("Choosing a number between " + str(first) + " and " + str(last) + ".")
print("The number is " + str(roll) + ".")