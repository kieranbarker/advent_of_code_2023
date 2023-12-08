from functools import cmp_to_key
from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()
lines = contents.splitlines()

for index, line in enumerate(lines):
    line = line.split(" ")
    line[1] = int(line[1])
    lines[index] = line


def get_char_count(str):
    char_count = {}

    for char in str:
        if char not in char_count:
            char_count[char] = str.count(char)

    return char_count


hand_types = (
    (1, 1, 1, 1, 1),  # high card
    (1, 1, 1, 2),  # one pair
    (1, 2, 2),  # two pair
    (2, 3),  # full house
    (1, 1, 3),  # three of a kind
    (1, 4),  # four of a kind
    (5,),  # five of a kind
)


def get_score(hand):
    char_count = get_char_count(hand)
    hand_type = tuple(sorted(char_count.values()))
    return hand_types.index(hand_type)


cards = "23456789TJQKA"


@cmp_to_key
def compare(a, b):
    score_a = get_score(a[0])
    score_b = get_score(b[0])

    diff = score_a - score_b

    if diff != 0:
        return diff

    # This clearly ain't workin'!
    for i in range(5):
        card_a = a[0][i]
        card_b = b[0][i]
        print(card_a, card_b)

        score_a = cards.index(card_a)
        score_b = cards.index(card_b)

        diff = score_a - score_b

        if diff != 0:
            return diff


lines.sort(key=compare)

for line in lines:
    print(line)

winnings = 0

for index, line in enumerate(lines):
    rank = index + 1
    bid = line[1]
    winnings += rank * bid

print(winnings)  # 246676029 is wrong
