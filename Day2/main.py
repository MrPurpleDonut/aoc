
MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

def format(text: str) -> tuple[int, list]:
    
    initalList = text.split(":")
    gameId = initalList[0]
    initalList.remove(gameId)
    gameId = gameId.replace("Game", "").strip()
    rgb = [0,0,0]
    for game in initalList[0].split(";"):
        for color in game.split(","):
            color = color.strip()
            if color.endswith("red"):
                rgb[0] = max(rgb[0], int(color.replace("red","").strip()))
            elif color.endswith("green"):
                rgb[1] = max(rgb[1], int(color.replace("green","").strip()))
            else:
                rgb[2] = max(rgb[2], int(color.replace("blue","").strip()))
        


    return int(gameId), rgb

def isValid(gameList: list) -> bool:
    return gameList[0] <= MAXRED and gameList[1] <= MAXGREEN and gameList[2] <= MAXBLUE

def main():
    f = open("input.txt", "r")
    sum = 0
    productSum = 0
    for line in f:
        num, gameList = format(line)
        productSum += gameList[0]*gameList[1]*gameList[2]
        if isValid(gameList):
            sum+=num
        
    print(sum)
    print(productSum)

if __name__ == "__main__":
    main()