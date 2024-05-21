from copy import deepcopy

def print2DArray(array: list):
    ourMap = {0:".", 1:"#"}
    for row in array:
        toPrint = ""
        for x in row:
            toPrint+=ourMap.get(x)
        print(toPrint)

def chunkify(f):
    ourMap = {".":0, "#":1}
    chunks = [[]]
    for line in f:
        if line != "\n":
            chunks[-1].append([ourMap.get(x) for x in line if x != "\n"])
        else:
            chunks.append([])
    return chunks

def rotate(chunk: list)->list:
    rotated = [list() for x in range(len(chunk[0]))]
    for row in chunk:
        for i in range(len(row)):
            rotated[i].append(row[i])
    

    return rotated

def verticalReflexion(chunk: list)->int:
    rotatedChunk = rotate(chunk)
    return horizontalReflexion(rotatedChunk)
 
def horizontalReflexion(chunk: list)->list:
    potentialVal = []
   
    for i in range(1, len(chunk)//2+1):
        if(chunk[:i] == chunk[i:2*i:][::-1]):
            potentialVal.append(i)

    for i in range(len(chunk)//2+1, len(chunk)):
        distance = len(chunk)-i
        if(chunk[i:] == chunk[len(chunk)-2*distance:i][::-1]):
            potentialVal.append(i)
    potentialVal.append(0)
    return potentialVal

def newHorizonalReflection(chunk: list, index)->int:
    for row in range(len(chunk)):
        for coulmn in range(len(chunk[row])):
            dc = deepcopy(chunk)
            dc[row][coulmn] =(1+chunk[row][coulmn])%2 
            values = horizontalReflexion(dc)
            for val in values:
                if val != 0 and val !=index:
                    return val        
    return 0


def main()->None:
    with open("input.txt", "r") as f:
        chunks = chunkify(f)

    chunkSum = 0
    smudgeSum = 0
    for chunk in chunks:
        vert = verticalReflexion(chunk)[0]
        horizon = horizontalReflexion(chunk)[0]
        chunkSum += vert + 100*horizon
        total = 100*newHorizonalReflection(chunk,horizon)+newHorizonalReflection(rotate(chunk), vert)
        if( total == 0):
            print2DArray(chunk)
            print()
        smudgeSum+= total
    print(chunkSum)
    print(smudgeSum)

if __name__ == "__main__":
    main()