# implementation of famous fibonacci recursively

def fib(num):
    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(8)) # 21