import os;
import re;

def Add(x, y):
    return x + y
    
def Sub(x, y):
    return x - y

def Mul(x, y):
    return x * y
    
def Div(x, y):
    return x / y

def IsEmpty(p_string):
    # at least one non-space character
    if not re.search("\S+", str(p_string)):
        return True
    return False;

def IsNumber(p_value):
    if re.search("\d+\.?\d*", str(p_value)):
        return True
    return False;

def SplitExpression(expression):
    items = []
    for char in expression:
        if not IsEmpty(char):
            items.append(char)

    num = ""
    builtItems = []
    for i in range(0, len(items)):
        currItem = items[i]
        if IsNumber(currItem):
            num = num + currItem
        else:
            if not IsEmpty(num):
                builtItems.append(float(num))
            num = ""
            builtItems.append(currItem)
        # end of array, push our num
        if i == len(items) - 1:
            if not IsEmpty(num):
                builtItems.append(float(num))

    return builtItems

    
def DoMath(x, y, symbol):
    x = float(x)
    y = float(y)
    # print("Do Math : "+str(x) + " " + str(y) + " " + symbol)
    if symbol == "+":
        return Add(x, y)
    elif symbol == "-":
        return Sub(x, y)
    elif symbol == "*":
        return Mul(x, y)
    elif symbol == "/":
        return Div(x, y)

def ResolveParentheses(splitExpression):
    newList = []
    currentNumber = ""
    symbol = ""
    fastForward = ""
    seedNum = ""
    finish = False

    for i in range(0, len(splitExpression)):
        if (IsNumber(fastForward)):
            # just skip til the next part
            if (i < fastForward):
                continue
            else:
                fastForward = ""

        currItem = splitExpression[i]
        if (currItem == "(" and not finish):
            for j in range(i+1, len(splitExpression)):
                currInnerItem = splitExpression[j]
                if IsNumber(currInnerItem):
                    if (IsEmpty(seedNum)):
                        # the first num after ( is the seed
                        seedNum = currInnerItem
                    else:
                        currentNumber = currInnerItem
                else:
                    if currInnerItem == ")":
                        fastForward = j + 1
                        finish = True
                        break
                    else:
                        symbol = currInnerItem
                        # the seed will hold the final value
                if (not IsEmpty(seedNum) and IsNumber(currentNumber) and not IsEmpty(symbol)):
                    # print(str(seedNum) + " " + str(currentNumber) + str(symbol))
                    seedNum = DoMath(seedNum, currentNumber, symbol)
                    # done resolving the parentheses eval, add it to the list
                    newList.append(seedNum)
        else:
            # not a parentheses eval, just add to list
            newList.append(currItem)
    return newList

# calling them shifts because the CPU is really shifting binary nums left or right in its register for Mul/Div
def ResolveShifts(splitExpression):
    newList = []
    currentNumber = ""
    symbol = ""
    fastForward = ""
    seedNum = ""
    finish = False

    for i in range(0, len(splitExpression)):
        if (IsNumber(fastForward)):
            # just skip til the next part
            if (i < fastForward):
                continue
            else:
                fastForward = ""

        currItem = splitExpression[i]
        # print("currItem "+str(currItem)+"\n")
        if (IsNumber(currItem) and not finish):
            # then peek forward, if the symbol is not div/mul, don't bother
            if (i + 1 < len(splitExpression)):
                nextItem = splitExpression[i + 1]
                # print("nextItem "+str(nextItem)+"\n")
                if (nextItem == "*" or nextItem == "/"):
                    symbol = nextItem
                    if (IsEmpty(seedNum)):
                        # the first num after ( is the seed
                        seedNum = currItem
                    nextNumber = splitExpression[i + 2]
                    # print("nextNumber "+str(nextNumber)+"\n")
                    seedNum = DoMath(seedNum, nextNumber, symbol)
                    # done resolving the parentheses eval, add it to the list
                    newList.append(seedNum)
                    fastForward = i + 3
                    finish = True
        else:
            newList.append(currItem)
    return newList

def ResolveAddSub(splitExpression):
    newList = []
    currentNumber = ""
    symbol = ""
    fastForward = ""
    seedNum = ""
    finish = False

    for i in range(0, len(splitExpression)):
        if (IsNumber(fastForward)):
            # just skip til the next part
            if (i < fastForward):
                continue
            else:
                fastForward = ""
        currItem = splitExpression[i]
        # print("currItem "+str(currItem)+"\n")
        if (IsNumber(currItem) and not finish):
            # then peek forward, if the symbol is not div/mul, don't bother
            if (i + 1 < len(splitExpression)):
                nextItem = splitExpression[i + 1]
                # print("nextItem "+str(nextItem)+"\n")
                if (nextItem == "+" or nextItem == "-"):
                    symbol = nextItem
                    if (IsEmpty(seedNum)):
                        # the first num after ( is the seed
                        seedNum = currItem
                    nextNumber = splitExpression[i + 2]
                    # print("nextNumber "+str(nextNumber)+"\n")
                    seedNum = DoMath(seedNum, nextNumber, symbol)
                    # done resolving the parentheses eval, add it to the list
                    newList.append(seedNum)
                    fastForward = i + 3
                    finish = True
        else:
            newList.append(currItem)
    return newList
    
def ResolveAllShifts(splitExpression):
    count = 0
    for item in splitExpression:
        if (item == "*" or item == "/"):
            count = count + 1
    for i in range(0, count):
        splitExpression = ResolveShifts(splitExpression)

    return splitExpression

def ResolveAllParentheses(splitExpression):
    count = 0
    for item in splitExpression:
        if (item == "("):
            count = count + 1
    for i in range(0, count):
        splitExpression = ResolveParentheses(splitExpression)

    return splitExpression

def ResolveAllAddSub(splitExpression):
    count = 0
    for item in splitExpression:
        if (item == "+" or item == "-"):
            count = count + 1
    for i in range(0, count):
        splitExpression = ResolveAddSub(splitExpression)

    return splitExpression

def Calculate(splitExpression):
    # first resolve all parentheses, making the expression 'flat'
    newExpressionList = ResolveAllParentheses(splitExpression)
    newExpressionList = ResolveAllShifts(newExpressionList)
    newExpressionList = ResolveAllAddSub(newExpressionList)
    # print(newExpressionList)
    return newExpressionList

def ValidateExpression(expression):
    for item in expression:
        if (item != "+" and item != "-" and item != "*" and item != "/" and item != " " and item != "(" and item != ")" and not IsNumber(item)):
            return False

    return True

def Main():
    # expression = "4/2+(1+2)+(5+5)"
    # expression = "(500+80) * 3000/800 + 30 + (5 + 5)"
    expression = input("Please enter your expression : ")
    if not ValidateExpression(expression):
        print("Sorry, but there are invalid characters in your input. Please try again with a valid expression. Thank you.")
    else:
        splitExpression = SplitExpression(expression)
        result = Calculate(splitExpression)
        print("The output of your expression is : \n")
        print(result[0])

    value = input(">>")

Main()