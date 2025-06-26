"""
    Find position of an element in a sorted array of infinite number.

    Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
    Source: Amazon interview Experience.
    Since array is sorted, the first thing clicks into mind is binary search, but the problem her is that we don't know
    size of array.

    if the array is infinite, that means we don't have proper bounds to apply binary search algorithm.
    Let low be pointing to first element and high pointing to 2nd element fo array, now compare
    key with high index element,

    -> if it is greater than high index element then copy high index in low index and double the high
        index.
    -> if it is smaller, than apply binary search on high and low indices found.

"""

"""
    Concept: Search in an Infinite Sorted Array
    
    In an infinite array, we cannot use normal binary search directly 
    because we don't know the upper boundary (length of array).
    
    Approach:
    1. Range Expansion (Exponential Search):
       - Start with a small range (start = 0, end = 1).
       - Double the end index (end = end * 2) until the target is 
         less than or equal to arr[end].
       - This helps us find a range where the target might exist.
    
    2. Binary Search:
       - Perform standard binary search between the found start and end.
       - This will locate the target efficiently within the valid range.
    
    Why it works:
    - Expanding range exponentially ensures we reach the region of interest in O(log n) time.
    - Binary search then finds the target in another O(log n) time.
    - Total time complexity is O(log n), very efficient for large/unknown-size arrays.
    
    Assumption: The array is sorted in ascending order.
"""
from typing import List

def infiniteArraySearch(data:List[int],target:int)->int:
    start = 0
    end = 1
    while target > data[end]:
        newStart = end +1
        end = end + (end-start+1)*2
        start = newStart

    return binarySearchWithStartEndIndex(data,target,start,end)

def binarySearchWithStartEndIndex(data:List[int],target:int,start:int,end:int)->int:
    while start <= end:
        mid = (start + end) // 2

        if target < data[mid]:
            end = mid - 1
        elif target > data[mid]:
            start = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    # assume this list is infinite in length here we only have finite number.
    # data = [3, 5, 7, 9, 10, 100, 130, 140, 160, 170, 180, 182, 190, 200,...]

    data = [3,5,7,9,10,100,130,140,160,170,180,182,190,200]
    target = 60

    ans = infiniteArraySearch(data,target)
    print(ans)