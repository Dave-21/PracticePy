def takeInput(s):
    myStack = []

    for i in s:
        if i in "({[":
            myStack.append(i)
        else:
            if len(myStack) > 0:
                temp = myStack.pop() + i
                if temp == "[]" or temp == "{}" or temp == "()":
                    continue
                else:
                    return False
            else:
                return False
    if len(myStack) > 0:
        return False
    return True
