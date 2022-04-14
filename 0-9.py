def vowels(word):
    vowel = "aeiouAEIOU"
    letters = ", ".join(character for character in word if character.lower() in vowel)

    print("Vowels: ", letters.lower())

vowels("Umuzi")




