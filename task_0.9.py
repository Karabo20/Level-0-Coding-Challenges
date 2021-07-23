#Task0.9

def vowel(keyword):
    for i in keyword:
        if i.islower() and i in "aeiou":
            print(i)
        else:
            if i.isupper() and i in "AEIOU":
                print(i)
vowel("moUntAin")
