"""
    Bubble Sort: Concept and Implementation

    Concept:
    - Bubble Sort is a simple comparison-based sorting algorithm.
    - It works by repeatedly swapping adjacent elements if they are in the wrong order.
    - In each pass through the array, the largest unsorted element "bubbles up" to its correct position at the end.
    - This process is repeated until the list is sorted.

    How it works:
    1. Compare each pair of adjacent elements in the array.
    2. Swap them if they are in the wrong order.
    3. After each full pass, the largest remaining unsorted element is placed at its correct sorted position.
    4. Continue the process for the remaining unsorted portion of the list.

    Time Complexity:
    - Worst case: O(n^2)
    - Best case (already sorted): O(n)
    - Space complexity: O(1) (in-place)

    Optimization:
    - If no swaps are made during a pass, the list is already sorted, and we can stop early.

    Use case:
    - Simple to implement and understand.
    - Not suitable for large datasets due to poor performance.

    Implementation below follows the optimized version with early exit.
"""

from typing import List

def bubbleSort(data:List[int])-> List[int]:

    for i in range(0, len(data)):
        for j in range(0,len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data

def bubbleSortOptimized(data: List[int]) -> List[int]:
    """
    Optimized Bubble Sort with early exit:
    - Stops early if no swaps are made in a pass (already sorted).
    """
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


if __name__=="__main__":
    data = [3,1,5,4,2,0,8,6,7,13,16,25,40,13]
    """
        In above array there is multiple 13 which is at index 9, and 13
        so in sorted array order of 13 will be maintained like above means
        13 at index 9 will be before of 13 of index 13 this concept is known as stability.
        that's why bubble sort is stable it follows the stability rule.
    """
    ans = bubbleSort(data)
    print(bubbleSortOptimized(data))
    print(ans)
