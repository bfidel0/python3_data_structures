# Sorted list that was rotated, find number of times it was rotated

def count_rotations(nums):
    '''
    Brute Force Solution
    '''
    position = 1
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position

        position += 1
    return 0
