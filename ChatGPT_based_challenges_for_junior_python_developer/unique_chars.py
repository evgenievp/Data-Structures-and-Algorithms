def has_unique_chars(s: str) -> bool:
    # Example: "hello" -> False, "world" -> True
    set_s = set(s)
    if len(s) == len(set_s):
        return True
    return False


s = "hello"
print(has_unique_chars(s)) # False
s = 'world'
print(has_unique_chars(s)) # True

