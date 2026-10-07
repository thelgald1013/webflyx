import random

# A Card is represented as a (rank, suit) tuple, e.g. ("Ace", "Spades")
Card = tuple[str, str]

class DeckOfCards:
    # Class-level constants shared by every instance of the deck
    SUITS: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS: list[str] = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self) -> None:
        # Cards are private; outside code can't touch this list directly
        self.__cards: list[Card] = []
        self.create_deck()

    def create_deck(self) -> None:
        # Build all 52 cards by pairing every suit with every ran
        for suit in DeckOfCards.SUITS:
            for rank in DeckOfCards.RANKS:
                cards = (rank, suit)
                self.__cards.append(cards)

    def shuffle_deck(self) -> None:
        # Shuffles cards in place
        random.shuffle(self.__cards)

    def deal_card(self) -> Card | None:
        # Deals the top card (end of the list) or None if the deck is empty
        if len(self.__cards) <= 0:
            return None
        else: 
            dealt_card = self.__cards.pop()
            return dealt_card 

def main():
  new_deck = DeckOfCards()
  new_deck.shuffle_deck()

  hand_size = 5
  hand = []
  # Deal hand_size cards one at a time from the shuffled deck
  for x in range(hand_size):
    card = new_deck.deal_card()
    hand.append(card)
  print("Your hand is:")
  for card in hand:
    rank, suit = card
    print(f"{rank} of {suit}")

main()
