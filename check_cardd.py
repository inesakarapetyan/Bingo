from cardd import generate_card

def is_win_col(card):
    for value in card.values():
        if sum(value) == 0:
            return True
        return False


def is_win_row(card):
    for value in card.values():
        
        if sum(value) == 0:
            return True
    return False

def is_win_diag(card):
    pass