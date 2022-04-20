def vowels(word):
    vowel = "aeiouAEIOU"
    result = set()
    string = ", "
    for character in word:
        if character in vowel:
         result.add(character)
    return (string.join(result))

print("Vowels:",vowels("UMUZI").lower())
