import setClasses

deck = setClasses.Deck()
colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Diamond", "Triangle"]

for i in colors:
    for k in shapes:
        for j in range(3):
            setClasses.Card(deck, (j + 1), k, i)


for i in range(deck.get_deck_size()//3):
    card_one = deck.draw_random()
    deck.remove_card(card_one)
    card_two = deck.draw_random()
    deck.remove_card(card_two)

    card_three = deck.find_set(card_one, card_two)
    
    if card_three != None:
        deck.remove_card(card_three)
        print("SET: ")
        card_one.print_card()
        print("---------")
        card_two.print_card()
        print("---------")
        card_three.print_card()
        print("---------")




