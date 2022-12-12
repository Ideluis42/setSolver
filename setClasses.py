import random

class Deck:
    def __init__(self) -> None:
        self.deck = []
    
    def add_card(self, card):
        self.deck.append(card)
    
    def print_deck(self):
        for i in self.deck:
            print(str(i.number) + i.shape + i.color)

    def remove_card(self, card):
        self.deck.remove(card)        

    def draw_random(self):
        idx = random.randint(0, len(self.deck) - 1)
        return self.deck[idx]

    def get_deck_size(self):
        return len(self.deck)

    def find_set(self, card_one, card_two):
        for i in range(len(self.deck)):
            card_three = self.deck[i]

            attributes_card_one = {
                "Number" : card_one.getNumber(),
                "Color" : card_one.getColor(),
                "Shape" : card_one.getShape()
            }
            
            attributes_card_two = {
                "Number" : card_two.getNumber(),
                "Color" : card_two.getColor(),
                "Shape" : card_two.getShape()
            }

            attributes_card_three = {
                "Number" : card_three.getNumber(),
                "Color" : card_three.getColor(),
                "Shape" : card_three.getShape()
            }

            if (attributes_card_one["Number"] == attributes_card_two["Number"]) and \
                (attributes_card_two["Number"] == attributes_card_three["Number"]):

                if (attributes_card_one["Color"] != attributes_card_two["Color"]) and \
                    (attributes_card_two["Color"] != attributes_card_three["Color"]) and \
                    (attributes_card_one["Color"] != attributes_card_three["Color"]):

                    if (attributes_card_one["Shape"] != attributes_card_two["Shape"]) and \
                        (attributes_card_two["Shape"] != attributes_card_three["Shape"]) and \
                        (attributes_card_one["Shape"] != attributes_card_three["Shape"]):
                        # All same number with different colors and different shapes           
                        return card_three
                        
                    elif attributes_card_one["Shape"] == attributes_card_two["Shape"] and \
                        attributes_card_two["Shape"] == attributes_card_three["Shape"]:
                        return card_three

                if (attributes_card_one["Shape"] != attributes_card_two["Shape"]) and \
                    (attributes_card_two["Shape"] != attributes_card_three["Shape"]) and \
                    (attributes_card_one["Shape"] != attributes_card_three["Shape"]): 
                        if attributes_card_one["Color"] == attributes_card_two["Color"] and \
                            attributes_card_two["Color"] == attributes_card_three["Color"]:
                            return card_three
            
            if attributes_card_one["Color"] == attributes_card_two["Color"] and \
                attributes_card_two["Color"] == attributes_card_three["Color"]:

                if attributes_card_one["Number"] != attributes_card_two["Number"] and \
                    attributes_card_two["Number"] != attributes_card_three["Number"] and \
                    attributes_card_one["Number"] != attributes_card_three["Number"]:

                    if attributes_card_one["Shape"] != attributes_card_two["Shape"] and \
                        attributes_card_two["Shape"] != attributes_card_three["Shape"] and \
                        attributes_card_one["Shape"] != attributes_card_three["Shape"]:
                        return card_three
                    
                    elif attributes_card_one["Shape"] == attributes_card_two["Shape"] and \
                        attributes_card_two["Shape"] == attributes_card_three["Shape"]:
                        return card_three
                            
                if (attributes_card_one["Shape"] != attributes_card_two["Shape"]) and \
                    (attributes_card_two["Shape"] != attributes_card_three["Shape"]) and \
                    (attributes_card_one["Shape"] != attributes_card_three["Shape"]):
                
                    if attributes_card_one["Number"] == attributes_card_two["Number"] and \
                        attributes_card_two["Number"] == attributes_card_three["Number"]:
                        return card_three

            if attributes_card_one["Shape"] == attributes_card_two["Shape"] and \
                attributes_card_two["Shape"] == attributes_card_three["Shape"]:

                if attributes_card_one["Number"] != attributes_card_two["Number"] and \
                    attributes_card_two["Number"] != attributes_card_three["Number"] and \
                    attributes_card_one["Number"] != attributes_card_three["Number"]:

                    if attributes_card_one["Color"] != attributes_card_two["Color"] and \
                        attributes_card_two["Color"] != attributes_card_three["Color"] and \
                        attributes_card_one["Color"] != attributes_card_three["Color"]:
                        return card_three

                    elif attributes_card_one["Color"] == attributes_card_two["Color"] and \
                        attributes_card_two["Color"] == attributes_card_three["Color"]:
                        return card_three
                            
                if (attributes_card_one["Color"] != attributes_card_two["Color"]) and \
                    (attributes_card_two["Color"] != attributes_card_three["Color"]) and \
                    (attributes_card_one["Color"] != attributes_card_three["Color"]):
                
                    if attributes_card_one["Number"] == attributes_card_two["Number"] and \
                        attributes_card_two["Number"] == attributes_card_three["Number"]:
                        # All same shape with different colors
                        return card_three

            if (attributes_card_one["Color"] != attributes_card_two["Color"]) and \
                (attributes_card_two["Color"] != attributes_card_three["Color"]) and \
                (attributes_card_one["Color"] != attributes_card_three["Color"]) and \
                attributes_card_one["Number"] != attributes_card_two["Number"] and \
                attributes_card_two["Number"] != attributes_card_three["Number"] and \
                attributes_card_one["Number"] != attributes_card_three["Number"] and \
                (attributes_card_one["Shape"] != attributes_card_two["Shape"]) and \
                (attributes_card_two["Shape"] != attributes_card_three["Shape"]) and \
                (attributes_card_one["Shape"] != attributes_card_three["Shape"]):
                return card_three
        
        return None 

class Card:
    def __init__(self, deck, number, shape, color):
        self.number = number
        self.shape = shape
        self.color = color

        deck.add_card(self)

    def getNumber(self):
        return self.number

    def getShape(self):
        return self.shape

    def getColor(self):
        return self.color

    def print_card(self):
        print("Number: " + str(self.number))
        print("Shape: " + self.shape)
        print("Color: " + self.color)

    

