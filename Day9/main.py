
def findDifferencesEnd(numList: list)->int:
    if all(x == 0 for x in numList):
        return 0
    
    newList = []
    for i in range(len(numList)-1):
        newList.append(numList[i+1]-numList[i])

    return numList[-1]+findDifferencesEnd(newList)

def findDifferencesBegining(numList: list)->int:
    if all(x == 0 for x in numList):
        return 0
    
    newList = []
    for i in range(len(numList)-1):
        newList.append(numList[i+1]-numList[i])

    return numList[0]-findDifferencesBegining(newList)


def main():
    f = open("small.txt", "r")
    listOfNums = []
    for line in f:
        a = line.split()
        b= [int(x) for x in a]
        listOfNums.append(b)

    differencesEnd =[findDifferencesEnd(x) for x in listOfNums]
    differencesBeginning = [findDifferencesBegining(x) for x in listOfNums]
    print(sum(differencesEnd))
    print(sum(differencesBeginning))

if __name__ == "__main__":
    main()