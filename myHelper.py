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
    isUps = x[0]
    if isUps.isupper():
        return "Upper case"
    else:
        return "Not upper case"

def isCaps(x):
    isCapitals = x
    sentLen = len(isCapitals)
    fullWord = isCapitals[0 : sentLen]
    if fullWord.isUpper():
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
