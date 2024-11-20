# a) FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz." For numbers that are multiples of both, print "FizzBuzz."
# Skills Tested:
# Loops
# Conditional statements
# Modulo operation
# Evaluation:
# A classic warm-up to test logic-building skills.
# Tests how well you can write clean and concise conditional logic.

num = 101
result = ""
for i in range(1, num):
    if i % 3 == 0 and i % 5 == 0:
        result += f"FizzBuzz {i}\n"
    if i % 5 == 0:
        result += f"Buzz {i}\n"
    elif i % 3 == 0:
        result += f"Fizz {i}\n"
print(result)
