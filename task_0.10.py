# Task 0.10
def common(phrase1, phrase2):
    common_letters = []
    for letter in phrase1:
        if letter in phrase2:
            common_letters.append(letter)
    print("Common letters:", ",".join(common_letters))
