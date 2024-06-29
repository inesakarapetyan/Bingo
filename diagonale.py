from cardd import generate_card

def check_diagonal_bingo(card):
    is_diagonal_bingo = True
    for i in range(5):
        if card[i] != 0:
            is_diagonal_bingo = False
            break

    return check_diagonal_bingo
    # if is_diagonal_bingo:
    #     is_diagonal_bingo = True
    #     for i in range(5):
    # else:
    #     is_diagonal_bingo = False
    # break

    # return is_diagonal_bingo(card)