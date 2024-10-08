# Recursive exercise from Hackerrank

def reverse(strng):
    if len(strng) == 0:
        return strng
    return strng[len(strng) - 1] + reverse(strng[:len(strng) - 1])


text = 'Hello World'
print(reverse(text)) # dlroW olleH