def safeGet(x: int, y: int, array: list)->str:
    if x >= 0 and y >= 0 and x < len(array) and y < len(array[x]):
        return array[x][y]
    return "0"
    


def isValid(row: int, start: int, length: int, array: list) -> bool:
    for i in range(length):
        values = []
        for j in range(3):
            for k in range(3):
                values.append(safeGet(row-1+k,start-1+i+j, array))
        for val in values:
            if(not val.isnumeric() and val != "."):
                return True
    return False

def generateNums(array: list) -> list:
    returnList = []
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y].isnumeric() and (y == 0 or not array[x][y-1].isnumeric()):
                entry = [0,x,y,0]
                val = array[x][y]
                count = 1

                while y+count < len(array[x]) and array[x][count+y].isnumeric():
                    val+=array[x][count+y]
                    count+=1

                entry[0] = int(val)
                entry[3] = count

                returnList.append(entry)

    return returnList

def generateGears(array: list) -> list:
    returnList = []
    for x in range(len(array)):
        for y in range(len(array[x])):
            val = array[x][y]
            if not val.isnumeric() and val != ".":
                returnList.append((x,y))
    return returnList

def getAdjacentNums(x: int, y: int, nums: list) -> list:
    #num in nums: val, x, starting y, length
    returnList = []
    for num in nums:
        for i in range(num[3]):
            if abs(x- num[1]) <= 1 and abs(num[2]+i-y) <=1:
                returnList.append(num[0])
                break


    return returnList

def main():
    f = open("input.txt", "r")
    characterArray = []
    for line in f:
        characterArray.append([x for x in line if not x == '\n'])

    nums = generateNums(characterArray)
    sum = 0
    for list in nums:
        if isValid(list[1], list[2], list[3], characterArray):
            sum+=list[0]
    print(sum)

    gearSum = 0
    gears = generateGears(characterArray)
    for gear in gears:
        adjacentNums = getAdjacentNums(gear[0], gear[1], nums)
        if(len(adjacentNums) == 2):
            gearSum += adjacentNums[0]*adjacentNums[1]
    print(gearSum)

    

if __name__ == "__main__":
    main()