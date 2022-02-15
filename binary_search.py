cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

# Brute Force Algo
""" def locate_card(cards, query):
    position = 0

    while True:
        if cards[position] == query:
            print(position)

        position += 1
        if position == len(cards):
            return -1


locate_card(cards, query) """
# Divide and Conquer Algo no repete in array empty array


def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo:", lo, "hi:", hi, "mid:", mid, "mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid_number + 1
    return -1
