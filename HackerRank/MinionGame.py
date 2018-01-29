if __name__ == "__main__":
    word = input()
    vowels = 'AEIOU'
    countk, counts = 0, 0
    length = len(word)
    for i in range(len(word)):
        if word[i] in vowels:
            countk += length - i
        else:
            counts += length - i
    if counts < countk:
        print("Kevin ", countk)
    elif countk < counts:
        print("Stuart ", counts)
    else:
        print("Draw")
    # slow method, thanks to myself
    # vowels = 'AEIOU'
    # countK = 0
    # countS = 0
    # kevin = []
    # stuart = []
    # length = len(word)
    # for i in range(length):
    #     if word[i] in vowels:
    #         for j in range(i, length):
    #             kevin.append(word[i:j + 1])
    #     else:
    #         for j in range(i, length):
    #             stuart.append(word[i:j + 1])
    # kevin = set(kevin)
    # stuart = set(stuart)
    # for sub in kevin:
    #     for i in range(length - len(sub) + 1):
    #         if word[i:i + len(sub)] == sub:
    #             countK += 1
    # for sub in stuart:
    #     for i in range(length - len(sub) + 1):
    #         if word[i:i + len(sub)] == sub:
    #             countS += 1
    # if countK < countS:
    #     print("Stuart " + str(countS))
    # else:
    #     print("Kevin " + str(countK))
