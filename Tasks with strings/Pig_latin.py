def pig_latin_converter(word):
    vowels = "aeiouAEIOU"

    if word[0] in vowels:
        pig_latin_word = word + "way"
    else:
        i = 0
        while i < len(word) and word[i] not in vowels:
            i += 1
        pig_latin_word = word[i:] + word[:i] + "ay"

    return pig_latin_word


word = input("Enter word to convert: ")
print("Input: ", word)
print("Output: ", pig_latin_converter(word))
