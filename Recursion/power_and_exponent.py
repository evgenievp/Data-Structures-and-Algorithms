def power(base, exponent):
    if exponent <= 0:
        return 1
    if exponent == 1:
        return base
    else:
        return power(base * 2, exponent - 1)


print(power(2, 3)) # 8