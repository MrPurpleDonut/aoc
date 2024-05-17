import cardHand
import wildCardHand

def preprocess(line: str):
    lineSplit = line.split()
    return [cardHand.cardHand(lineSplit[0],int(lineSplit[1])), wildCardHand.wildCardHand(lineSplit[0],int(lineSplit[1]))]


def main():
    f = open("input.txt", "r")
    stuff = [preprocess(line) for line in f]
    wildHands = [x[1] for x in stuff]
    hands =[x[0] for x in stuff]
    hands.sort()
    wildHands.sort()

    bidSum = 0
    wildSum = 0
    for i in range(len(hands)):
        bidSum+=(i+1)*(hands[i].bid)
        wildSum+=(i+1)*(wildHands[i].bid)
    print(bidSum)
    print(wildSum)


if __name__ == "__main__":
    main()