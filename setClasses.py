import random

class Deck:
    def __init__(self) -> None:
        self.deck = []
    
    def add_card(self, card):
        self.deck.append(card)
    
    def print_deck(self):
        for i in self.deck:
            print(str(i.number) + i.shape + i.color)
            

    def draw_random(self):
        idx = random.randint(0, len(self.deck))
        return self.deck.pop(self.deck[idx])

    def get_deck_size(self):
        return len(self.deck)


class Card:
    def __init__(self, deck, number, shape, color):
        self.number = number
        self.shape = shape
        self.color = color

        deck.add_card(self)

    def print_card(self):
        pass

    

