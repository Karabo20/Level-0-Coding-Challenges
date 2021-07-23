# Task 0.10
def common(phrase1, phrase2):
    com_letters = []
    print("Common letters: ", end="")
    for i in phrase1:
        if i in phrase2:
            com_letters.append(i)
    print(",".join(com_letters))
common("computers", "house")
