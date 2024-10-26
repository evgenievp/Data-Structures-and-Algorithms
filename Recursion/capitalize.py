def capitalize_words(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_words(arr[1:])



arr = ['some', 'random', 'sentence']
print(capitalize_words(arr)) # ['SOME', 'RANDOM', 'SENTENCE']
