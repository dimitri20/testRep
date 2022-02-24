import random

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
testStr = ""
generatedStrings = []

for i in range(23982224839372800):
    
    for i in range(10):
        testStr += random.choice(string)
    
    if testStr not in generatedStrings:
        generatedStrings.append(testStr)
        print(testStr)
        
    testStr = ""


def generateStrings():
    string = ""
    for i in range(97, 123):
        string+=chr(i)
    
    for i in range(65, 91):
        string+=chr(i)
    
    for i in range(10):
        string += str(i)
        
    return string
