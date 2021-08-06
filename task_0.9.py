# TASK0.9
def vowels_only(keyword):
    print(keyword)
    vowel = ""
    for i in range(len(keyword)):
        if (keyword[i].lower() in keyword) and (keyword[i].lower() not in vowel):
            vowel = vowel + keyword[i].lower()
        elif (keyword[i] not in keyword[i+1:]) and (keyword[i] not in vowel):
            vowel = vowel + keyword[i]
    print(vowel)
