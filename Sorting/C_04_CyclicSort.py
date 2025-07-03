"""
    ================================
     CYCLIC SORT - CONCEPT EXPLAINED
    ================================

    Cyclic sort is a highly efficient in-place sorting algorithm
    designed specifically for arrays containing integers in a fixed
    known range — typically 1 to n or 0 to n-1, often without duplicates.

    ============================
     HOW IT WORKS
    ============================
    - Every number in the array ideally belongs at a specific index:
        * If the range is 1..n, correct index = number - 1
        * If the range is 0..n-1, correct index = number

    - The algorithm places each element at its correct index
      by swapping it with the element at its target position.

    - This process is repeated until all elements are at their correct
      positions.

    - It's called "cyclic" sort because elements move in cycles to reach
      their correct places with minimal passes over the array.

    ============================
     EXAMPLE
    ============================
    Given: [3, 1, 2, 4]

    Step-by-step:
    1. i = 0
       value = 3
       correct index = 2
       swap arr[0] with arr[2]
       Result: [2, 1, 3, 4]

    2. i = 0
       value = 2
       correct index = 1
       swap arr[0] with arr[1]
       Result: [1, 2, 3, 4]

    3. i = 0
       value = 1
       correct index = 0
       already correct

    4. Move to next indices — all are in place.

    Final sorted array: [1, 2, 3, 4]

    ============================
     PSEUDOCODE
    ============================
    i = 0
    while i < len(array):
        correct_index = array[i] - 1
        if array[i] != array[correct_index]:
            swap(array, i, correct_index)
        else:
            i += 1

    ============================
     CHARACTERISTICS
    ============================
    - Time Complexity: O(n)
      Each element is moved at most once.

    - Space Complexity: O(1)
      Sorts in-place without extra memory.

    - Best suited for:
      * Arrays with numbers in known ranges.
      * Solving problems like finding missing numbers, duplicates.

    ============================
     ADVANTAGES
    ============================
    - Very simple and easy to implement.
    - Extremely efficient (linear time) for the intended problem type.
    - Great for interview questions about array manipulation.

    ============================
     LIMITATIONS
    ============================
    - Requires knowing the value range.
    - Assumes elements fit the target range (usually no gaps, unless adapted).
    - Needs to handle duplicates carefully in variations.

"""

from typing import List

def cyclicSort(data:List[int])->List[int]:
    sortedData= data.copy()
    i = 0
    while i< len(data):
        correct = sortedData[i] - 1
        if i != correct:
            sortedData[i],sortedData[correct]= sortedData[correct],sortedData[i]
        else:
            i+=1
    return sortedData


if __name__=="__main__":
    data = [5,4,3,2,1]
    result = cyclicSort(data)
    print(result)