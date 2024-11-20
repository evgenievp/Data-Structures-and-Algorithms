def is_palindrome(s: str) -> bool:
    # Example input: "racecar" -> True
    reversed = ""
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]
    if s == reversed:
        return True


s = "racecar"
print(is_palindrome(s)) # True
# solution can be modified for lowercase and uppercase letters.

