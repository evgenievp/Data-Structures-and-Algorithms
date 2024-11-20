def analyze_file(filename: str) -> dict:
    # Output: {'lines': 10, 'words': 50, 'characters': 300}
    with open(filename, "r") as f:
        rows = 0
        words = 0
        characters = 0
        for row in f.readlines():
            rows += 1
            for i in range(len(row)):
                characters += 1
            word_new_count = row.split()
            words += len(word_new_count)

    dict = {"lines": rows, "words": words, "characters": characters}
    return dict


print(analyze_file("test.txt"))
