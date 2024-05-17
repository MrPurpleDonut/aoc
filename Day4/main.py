import math

def preprocess(line: str) -> list:
    first = line.split(":")
    second = first[1].split("|")
    returnList = [second[0].split(), second[1].split()]
    return returnList

def scoreCard(card: list)->int:
    count = 0
    for val in card[0]:
        if(val in card[1]):
            count+=1
    return count


def main():
    f = open("input.txt", "r")
    cards =[]
    for line in f:
        cards.append(preprocess(line))
    cardSum = 0
    for card in cards:
        cardSum+=math.floor(2**(scoreCard(card)-1))
    print(cardSum)

    allCard = [1]*len(cards)
    for i in range(len(cards)):
        num = scoreCard(cards[i])
        for j in range(num):
            allCard[i+j+1] += allCard[i]
    
    print(sum(allCard))

    
if __name__ == "__main__":
    main()