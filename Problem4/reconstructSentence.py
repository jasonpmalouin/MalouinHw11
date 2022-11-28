# reconstructSentence.py
# Created By Jason Malouin
# This program accepts two text files as inputs and creates a list that concatenates words from both files in an alternating fashion. Words are appended beginning at the end of each file
#Usage: python3 reconstructSentence.py <file1> <file2>

import sys

def createList(fileName):
    f = open(fileName, "r")
    contents = f.read()
    words = contents.split()
    f.close()
    return words

def createOutput(list1, list2):
    output = []
    outputIndex = 0
    inputIndex = -1
    for count in range(len(list1)):
        output.insert(outputIndex, list1[inputIndex])
        inputIndex=inputIndex-1
        outputIndex=outputIndex+2

    outputIndex = 1
    inputIndex = -1
    for count in range(len(list2)):
        output.insert(outputIndex, list2[inputIndex])
        inputIndex=inputIndex-1
        outputIndex=outputIndex+2

    return output

def writeOutput(outputList):
    f = open("output.txt", "w")
    for word in outputList:
        f.write(word)
        f.write(' ');
    f.close()

if len(sys.argv) > 2:
    list1 = createList(sys.argv[1])
    print("List 1 Is:")
    print(list1)
    print("")
    list2 = createList(sys.argv[2])
    print("List 2 Is:")
    print(list2)
    print("")
    outputList = createOutput(list1, list2)
    print("The Output Is:")
    print(outputList)
    writeOutput(outputList)
else:
    print("Insufficient Arguments")
    print("Usage: python3 reconstructSentence.py <file1> <file2>")


    

