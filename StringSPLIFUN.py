


def StringSplit(InString, Char):

    StringList = []
    prevCharIndex = 0

    for index in range(len(InString)):
        if InString[index] == Char:
            StringList.append(InString[prevCharIndex:index])
            prevCharIndex = index + 1


    StringList.append(InString[prevCharIndex:])



    return StringList





