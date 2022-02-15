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

# simple Binary Search


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# DC finding first and last position in an array LC 34


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return 'found'
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid+1] == target:
                return "right"
            return 'found'
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
