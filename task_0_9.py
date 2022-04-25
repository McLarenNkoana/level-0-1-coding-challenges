def vowels(word):
    vowel = "aeiouAEIOU"
    result = set()
    string = ", "
    for character in word:
        if character in vowel:
         result.add(character.lower())
    print("Vowels:",string.join(result).lower())

vowels("UMUZI")
