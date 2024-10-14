def takeInput(s):
    tempConcat = ""
    counter = 1
    for i in s:
        tempConcat += i
        if tempConcat in s[counter::]:
            if tempConcat * (len(s)//len(tempConcat)) == s:
                return tempConcat

        counter += 1
