def common(input1, input2):
    word1 = set(input1)
    word2 = set(input2)
    characters = tuple(word1 & word2)
    print("Common letters: {}".format(characters))

common("house", "computers")

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
