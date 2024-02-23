def count_vowels(word):
    vowels = "aeiou"
    vowel_counts = {"a": 0, "e": 0, "i": 0,"o": 0,"u": 0}

    for letter in word:
        if letter.lower() in vowels:
            vowel_counts[letter.lower()] += 1

    total = sum(vowel_counts.values())

    print("Total vowels: ", total)
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")


word = input("Enter a word: ")
count_vowels(word)