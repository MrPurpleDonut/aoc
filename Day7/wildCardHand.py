class wildCardHand:

    def __init__(self, hand: str, bid: int) -> None:
        self.hand = wildCardHand.convertHand(hand)
        self.bid = bid
        potentialHands = []
        for i in range(14):
            potentialHands.append(wildCardHand.rankHand([x if x!= 0 else i for x in self.hand]))
        self.handRank = max(potentialHands)

    def __eq__(self, obj):
        return self.hand == obj.hand
    
    def __lt__(self, obj):
        if(self.handRank != obj.handRank):
            return self.handRank < obj.handRank
        for i in range(5):
            if self.hand[i] != obj.hand[i]:
                return self.hand[i] < obj.hand[i]
        return False
    
    def __repr__(self) -> str:
        return str(self.hand)

    @staticmethod
    def rankHand(hand: list)->int:
        handMap = {"High Card": 0, "Pair": 1, "Two Pair": 2, "3OAK": 3, "Full House": 4, "4OAK": 5, "5OAK": 6}
        counts = [hand.count(card) for card in set(hand)]
        handValue = "High Card"
        if 5 in counts:
            handValue = "5OAK"
        elif 4 in counts:
            handValue="4OAK"
        elif 3 in counts and 2 in counts:        
            handValue = "Full House"
        elif 3 in counts:
            handValue = "3OAK"
        elif counts.count(2) == 2:
            handValue = "Two Pair"
        elif 2 in counts:
            handValue = "Pair"
        return handMap.get(handValue)

    @staticmethod
    def convertHand(hand: str)->list:
        cardMappings = {"T":10, "J": 0, "Q":11, "K":12, "A":13}
        returnList = []
        for x in hand:
            if x.isnumeric():
                returnList.append(int(x))
            else:
                returnList.append(cardMappings.get(x))

        return returnList
