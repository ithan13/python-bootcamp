from random import choice
from tokenize import endpats


# Return a list of 52 strings containing a standard deck
def create_deck() -> list[str]:
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    deck = [
        (rank + suit)
        for rank in ranks
        for suit in suits
    ]
    return (deck)
# print(create_deck())

# Remove count return count cards from the start from deck
def draw_top(deck: list[str], count: int=1)-> list[str]:
    return deck.pop(0)
# print(draw_top(deck,))
# print(deck)

# Remove and return count cards from the end of the deck
# .pop removes the value wrt the specified index
def draw_bottom(deck: list[str], count: int=1) -> list[str]:
    return deck.pop(-1)
# print(draw_bottom(deck))
# print(deck)

# Remove and return count random cards from the deck
# .remove is used because no index
def draw_random(deck: list[str], count: int=1) -> list[str]:
    random_options = choice(deck)
    deck.remove(random_options)
    return random_options
# print(draw_random(deck))
# print(deck)

# Print all cards in deck
def show(deck):
    for card in deck:
        print(card)

deck = create_deck()
show(deck)
