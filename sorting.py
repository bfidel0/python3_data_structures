import random
import time


in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

nums = [99, 10, 56, 3, 4, 89, 32, 55, 879, 21, 22, 23, 45]

# bubble sort O(n^2) gross

#start = time.time()


def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


#end = time.time()

# bubble_sort(nums)
# print(end-start)


# Insertion Sort also gross
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

# Merge Sort unboundlocalerror rn


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums

# Helper function for Merge Sort


def merge(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            nums1_tail = nums1[i:]
            nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail


# Quick Sort O(nlogn) since we aren't changing the list usualy O(n)
def quicksort(nums, start=0, end=None):
    if end is None:
        # create new list so we don't change current one
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)
    return nums

# Helper for quick sort


def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    l, r = start, end - 1
    while r > l:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
