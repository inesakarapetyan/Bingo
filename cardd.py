from random import sample

def generate_card():
    card = {
        'B': sorted(sample(range(1, 16), k=5)),
        'I': sorted(sample(range(16, 31), k=5)),
        'N': sorted(sample(range(31, 46), k= 5)),
        'G': sorted(sample(range(46, 61), k=5)),
        'O': sorted(sample(range(61, 76), k=5))
    }

    return card


def show_card(card):
    for key in card:
        print(f'{key:>5}', end='')

    print()

    for i in range(len(card)):
        for elem in card.values():
            print(f'{elem[i]:>5}', end='')
        print()


def main():
    bingo_card = generate_card()
    show_card(bingo_card)

if __name__ == '__main__':
    main()    

