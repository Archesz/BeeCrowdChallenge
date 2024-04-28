class Deck():

    def __init__(self, n):
        self.cards = self.getCards(n)
        self.top = self.cards[0]
        self.bot = self.cards[-1]
        self.discarteds = []
    
    def getCards(self, n):
        cards = []
        for i in range(1, n + 1):
            cards.append(f"{i}")
        
        return cards

    def __len__(self):
        return len(self.cards)

    def discard(self):
        self.discarteds.append(self.top)
        self.cards.pop(0)
        self.top = self.cards[0]

    def move(self):
        self.cards.append(self.cards[0])
        self.cards.pop(0)
        self.top = self.cards[0]
        self.bot = self.cards[-1]

    def response(self):
        print(f"Discarded cards: {', '.join(self.discarteds)}")
        print(f"Remaining card: {self.cards[0]}")

n = int(input())

while n != 0:

    deck = Deck(n)

    while len(deck) >= 2:
        deck.discard()
        deck.move()

    deck.response()

    n = int(input())