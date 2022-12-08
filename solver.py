import setClasses

deck = setClasses.Deck()
colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square", "Triangle"]

for i in colors:
    for k in shapes:
        for j in range(3):
            setClasses.Card(deck, (j + 1), k, i)

print(deck.get_deck_size())
deck.print_deck()