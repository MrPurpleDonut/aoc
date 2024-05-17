import itertools
import math

def preprocess(lines: list)->dict:
    returnDict ={}
    for line in lines:
        tempList = line.replace("\n", "").replace(" ", "").split("=")
        destinations = tempList[1].replace("(", "").replace(")","").split(",")
        returnDict[tempList[0]] = destinations
    return returnDict

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    rightLeft = lines[0].replace("\n", "")
    directions =[1 if x == "R" else 0 for x in rightLeft]
    print(directions)

    nodes= preprocess(lines[1:])
    currentLocation = [x for x in nodes.keys() if x[-1] == "A" ]
    numVisisted = 0
    numIterations = []
    isValid = [True]*len(currentLocation)
    numValid = len(currentLocation)
    while True:
        for direction in itertools.cycle(directions):
            for i in range(len(currentLocation)):
                if isValid[i]:
                    currentLocation[i] = nodes.get(currentLocation[i])[direction]
            numVisisted += 1
            for i in range(len(currentLocation)):
                if currentLocation[i][-1] == "Z":
                    numIterations.append(numVisisted)
                    isValid[i] = False
                    numValid-=1
                    currentLocation[i] = "PASS"
            if numValid == 0:
                break
        break


    print(numIterations)


if __name__ == "__main__":
    main()