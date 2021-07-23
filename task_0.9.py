#Task 0.9
def vowel_only(keyword):
    vowels = [] 
    print("Vowels: ", end="")
    for i in keyword:
        if i.islower() and i in "aeiou":
            vowels.append(i)
        else:
            continue
    print(",".join(vowels))
vowel_only("Umuzi")
