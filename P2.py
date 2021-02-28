import os;
import re;

def IsNumber(p_value):
    if re.search("\d+\.?\d*", str(p_value)):
        return True
    return False;

def IsEmpty(p_string):
    # at least one non-space character
    if not re.search("\S+", str(p_string)):
        return True
    return False;

def SplitNumber(number):
    digits = []
    for digit in number:
        digits.append(digit)

    return digits

def ValidateArray(digitsArray):
    prevDigit = 0
    currDigit = 0
    nextDigit = 0
    for i in range(1, len(digitsArray)):
        currDigit = int(digitsArray[i])
        prevDigit = int(digitsArray[i-1])
        if i+1 < len(digitsArray):
            nextDigit = int(digitsArray[i+1])
        else:
            nextDigit = int(digitsArray[len(digitsArray)-1])
        if currDigit < prevDigit or currDigit > nextDigit:
            return False
    return True

def Resolve(digitsArray):
    newList = digitsArray
    prevDigit = ""
    currDigit = ""
    nextDigit = ""

    for i in range(0, len(digitsArray)):
        currDigit = int(digitsArray[i])
        if (i > 0):
            prevDigit = int(digitsArray[i-1])

        if not IsEmpty(prevDigit):
            while (prevDigit > currDigit):
                prevDigit = prevDigit - 1
            newList[i-1] = prevDigit
            # print("currDigit: "+str(currDigit))
            # print("\nprevDigit: "+str(prevDigit))
            # print("\nnextDigit: "+str(nextDigit))
    return newList

def SnapToNearestLargest(digitsArray, inputNum):
    inputNumArray = []
    for x in inputNum:
        inputNumArray.append(str(x))

    fillNinesFrom = ""
    for i in range(0, len(digitsArray)):
        if int(digitsArray[i]) < int(inputNumArray[i]):
            if i < len(digitsArray):
                fillNinesFrom = i+1
                break
    # print(fillNinesFrom)
    if IsNumber(fillNinesFrom):
        for i in range(int(fillNinesFrom), len(digitsArray)):
            digitsArray[i] = "9"

    return digitsArray

def ToString(digitsArray):
    message = ""
    for i in range(0, len(digitsArray)):
        currDigitStr = str(digitsArray[i])
        if i == 0 and currDigitStr == "0":
            continue
        message = message + currDigitStr

    return message

def Main():
    # inputNum = "23245" #  22999
    # inputNum = "11235888" # 11235888
    # inputNum = "111110" # 99999
    # inputNum = "33245" #  29999

    inputNum = input("Hello Peter, please input a number between 1 and 10 ^ 18 and I will give you the last number you checked.\n")
    if (not IsNumber(inputNum)):
        print("Sorry Peter, the 'number' you entered is not a valid number. Please give me something else. Thanks.")
    else:
        digitsArray = SplitNumber(inputNum)
        # digitsArray = SplitNumber("12345")
        while (not ValidateArray(digitsArray)):
            digitsArray = Resolve(digitsArray)

        digitsArray = SnapToNearestLargest(digitsArray, inputNum)
        finalNum = ToString(digitsArray)
        print("Your last checked number while meditating was : \n")
        print(finalNum)
        input(">>")


    # nines = []
    # digitsStr = ""
    # for x in digitsArray:
        # nines.append("9")
        # digitsStr = digitsStr + str(x)

    # if str(digitsArray[0]) != "9":
        # nines[0] = str(digitsArray[0])
    # ninesStr = ""
    # for x in nines:
        # ninesStr = ninesStr + str(x)
    # ninesInt = int(ninesStr)

    # finalResult = ""
    # if ninesInt < int(inputNum) and ninesInt > int(digitsStr):
        # finalResult = ninesStr
    # else:
        # finalResult = digitsStr
    # print(finalResult)
    # number = input("Hello Peter, please input a number between 1 and 10 ^ 18 and I will give you the last number you checked.\n")
    # if (not IsNumber(number)):
        # print("Sorry Peter, the 'number' you entered is not a valid number. Please give me something else. Thanks.")
    # else:
        # digitsArray = SplitNumber(number)
        # result = Resolver(digitsArray)
        # finalString = ""
        # for digit in result:
            # finalString = finalString + str(digit)
        # print("Your last checked number while meditating was : \n")
        # print(finalString)

    # value = input(">>")
Main()