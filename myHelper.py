from collections import Counter

def maxVal(x, y):
    if x > y:
        return x
    else:
        return y

def minVal(x, y):
    if x < y:
        return x
    else:
        return y

def squared(x):
    if x > 0:
        return x * x

def squareRoot(x):
    if x > 0:
       return x**(1/2)

def addition(x, y):
    if x > 0 and y > 0:
        return x + y

def subtraction(x, y):
    if x > 0 and y > 0:
        return x - y

def multiplication(x, y):
    if x > 0 and y > 0:
        return x * y

def division(x, y):
    if x > 0 and y > 0:
        return x / y

def remainder(x, y):
    return x % y

def strLenWhiteSpace(x):
    return len(x)

def strLen(x):
    x = x.replace(" ", "")
    return len(x)

def isUpperCase(x):
    upWord = x[0]
    if upWord.isupper():
        return "Upper case"
    else:
        return "Not upper case"

def isCaps(x):
    isCapitals = x
    sentLen = len(isCapitals)
    fullWord = isCapitals[0 : sentLen]
    if fullWord.isupper():
        return "Capitals"
    else:
        return "Not capitals"

def containsInStr(x, y):
    if y.lower() in x.lower():
        return "Word is in string"
    else:
        return "Word is NOT in string"

def removeWord(x, y):
    return x.replace(x, y)

def evenOdd(x):
    if (x % 2) == 0:
       return str(x) + " is even"
    else:
        return str(x) + " is odd"

def Mean(numbers):
    speedSum = sum(numbers)
    listlen = len(numbers)
    answer = speedSum / listlen
    return answer

def Median(numbers):
    listlen = len(numbers)
    myEven = False

    if (listlen % 2) == 0:
        mean = listlen / 2
        myEven = True
    else:
        mean = listlen / 2 - 0.50
        myEven = False

    newMean = int(mean)
    plusOne = newMean - 1
    if myEven:
        return numbers[plusOne], "and", numbers[newMean]
    else:
        return numbers[newMean]

def Mode(numbers):
    mostCommon = Counter(numbers)
    return mostCommon.most_common(1)

def countCaps(x):
    count = 0
    for i in x:
        if i.isupper():
            count += 1
    return str(count) + " Capital letters"

def bubbleSort(list):
    for j in range(0, len(list) - 1):
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                swap = list[i]
                list[i] = list[i + 1]
                list[i + 1] = swap

    return list

def listSum(x):
    count = 0
    for i in x:
        count += i

    return count

def arrayBigger(x, y):
    x = listSum(x)
    y = listSum(y)

    if x > y:
        return "List one is bigger"
    else:
        return "List two is bigger"

def addListSum(x, y):
    x = listSum(x)
    y = listSum(y)

    return x + y

def subtractListSum(x, y):
    x = listSum(x)
    y = listSum(y)

    return x - y

def numInList(x, theList):
    if x in theList:
        return True
    else:
        return False

def checkNegative(x):
    if x < 0:
        return True
    else:
        return False

def powerOf(x, y):
    return x**y

def nextWholeNumber(x):
    a = x - int(x)
    remain = 1 - a
    if a > 0.5:
        return x + remain
    else:
        return x - a
