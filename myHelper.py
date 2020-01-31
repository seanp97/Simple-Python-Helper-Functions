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

def strLen(x):
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
