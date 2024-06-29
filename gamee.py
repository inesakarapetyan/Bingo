from cardd import generate_card, show_card
from random import shuffle
from check_cardd import is_win_col, is_win_diag, is_win_row
from diagonale import check_diagonal_bingo
# from time import sleep

def game(card):
    box = list(range(1, 76))
    shuffle(box)

    while not is_win_col(card):
        number = box.pop()
        for value in card.values():
            if number in value:
                value[value.index(number)] = 0
        
        print(number)
        show_card(card)


card = generate_card()
game(card)
