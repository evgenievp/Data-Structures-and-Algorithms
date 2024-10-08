# Recursive solution - palindrome checker.

def isPalindrome(ss):
    if len(ss) == 0:
        return True
    if ss[0] != ss[len(ss) - 1]:
        return False
    return isPalindrome(ss[1:-1])


ss = 'азобичаммачибоза'
print(isPalindrome(ss)) # True
ss = 'Hello world!'
print(isPalindrome(ss)) # False
