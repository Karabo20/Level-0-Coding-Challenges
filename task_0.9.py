#Task0.9
def vowel_only(keyword):
    vowels = [] 
    for letter in keyword:
        if letter in "AEIOU" or letter in "aeiou":
            vowels.append(letter)
        else:
            continue
    print("Vowels:", ",".join(vowels))
vowel_only("Umuzi")
