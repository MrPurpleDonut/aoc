

characterMap ={"|": ([1,0], [-1,0]),
               "-": ([0,1], [0,-1]),
               "L": ([-1,0], [0,1]),
               "J": ([-1,0], [0,-1]),
               "7": ([1,0], [0,-1]),
               "F": ([1,0], [0,1])}


def printBoard(board: list[list])->None:
    for row in board:
        text = ""
        for x in row:
            text += x
        print(text)

def findStart(board: list[list])->tuple[int, int]:
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == "S":
                board[row][column] = "F"
                return row, column


def shoelaceSum(cordinates: list[tuple])->int:
    areaSum = 0
    size = len(cordinates)
    for i in range(size):
        areaSum+= cordinates[i][0]*(cordinates[(i-1)% size][1]-cordinates[(i+1)%size][1])

    return abs(areaSum/2)

def main()->None:
    f = open("input.txt", "r")
    board = [[x for x in line if x != "\n"] for line in f]

    intialRow, intialColumn = findStart(board)
    pathBoard = [[0 for _ in board[0]] for _ in board]

    cordinates = []
    areaSum = 0
    count = 0
    prevRow, prevColumn = -1, -1
    currentRow, currentColumn = intialRow, intialColumn
    while True:
        potentialMoves = characterMap.get(board[currentRow][currentColumn])
        if currentRow+potentialMoves[0][0] == prevRow and currentColumn+potentialMoves[0][1] == prevColumn:
            prevRow, prevColumn = currentRow, currentColumn
            currentRow += potentialMoves[1][0]
            currentColumn += potentialMoves[1][1]
        else:
            prevRow, prevColumn = currentRow, currentColumn
            currentRow += potentialMoves[0][0]
            currentColumn += potentialMoves[0][1]
        count+=1
        pathBoard[currentRow][currentColumn] = 1
        cordinates.append((currentRow, currentColumn))
        if currentRow == intialRow and currentColumn == intialColumn:
            break

    print(count/2)

    for row in range(len(board)):
        for column in range(len(board[row])):
            if(pathBoard[row][column]) == 0:
                board[row][column] = "."

    area = shoelaceSum(cordinates)

    print(area-count/2+1)
           




if __name__ == "__main__":
    main()