def common(input1, input2):
    word1 = set(input1)
    word2 = set(input2)
    characters = (", ").join(word1 & word2)
    print("Common letters: {}".format(characters))

common("house", "computers")
