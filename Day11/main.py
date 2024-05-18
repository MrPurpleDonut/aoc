

def findGalaxies(sky: list[list])->list[tuple]:
    cords = []
    for row in range(len(sky)):
        for column in range(len(sky[row])):
            if sky[row][column] == "#":
                cords.append((row, column))
    return cords

def findExpansions(sky: list[tuple], numOfRows: int, numOfColumns: int)->tuple[list,list]:
    rowGalaxies = set(sky[x][0] for x in range(len(sky)))
    columnGalaxies = set(sky[x][1] for x in range(len(sky)))
    expandedRows = [i for i in range(numOfRows) if i not in rowGalaxies]
    expandedColumns =[i for i in range(numOfColumns) if i not in columnGalaxies]
    return expandedRows, expandedColumns    

def main()->None:
    with open("input.txt", "r") as f:
        fileContents = [[x for x in line if x != "\n"] for line in f]
    cords = findGalaxies(fileContents)
    rowExpansions, columnExpansions = findExpansions(cords,len(fileContents), len(fileContents[0]))
    print(rowExpansions, columnExpansions)
    totalDistance = 0
    for i in range(len(cords)-1):
        for j in range(i+1,len(cords)):
            y1, y2 = min(cords[i][1], cords[j][1]), max(cords[i][1], cords[j][1])
            x1, x2 = min(cords[i][0], cords[j][0]), max(cords[i][0], cords[j][0])
            dist = x2+y2-x1-y1

            for x in range(x1,x2):
                if x in rowExpansions:
                    dist +=1000000-1
                    
            for x in range(y1,y2):
                if x in columnExpansions:
                    dist +=1000000-1
                    
            totalDistance+=dist

    print(totalDistance)

if __name__ == "__main__":
    main()