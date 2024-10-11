import random
arr = []

# Fill array with random numbers.
def fill_with_random_numbers():
    for _ in range(100):
        arr.append(random.randint(1, 1000))
    return arr
