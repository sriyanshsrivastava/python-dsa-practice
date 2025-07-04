"""
    Find the Duplicate Number

    Given an array of integers nums containing n+1 integers where each integer is in the range
    [1,n] inclusive.

    There is only one repeated number in nums, return this repeated number.

   You must solve problem without modifying tha array nums and  uses only constant extra space.

   Example:
        Input: nums = [1,3,4,2,2]
        Output: 2
"""




from typing import List
from UtilityTools import swap

def findDisappearedNumbers(data:List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(data):
        correctValueAtIndex = data[i]-1
        if data[i]!= data[correctValueAtIndex]:
            swap(data,i,correctValueAtIndex)
        else:
            i+=1


    for j in range(0, len(data)):
        if data[j] != j+1:
            return data[j]

    return -1


if __name__=="__main__":
    data = [1,3,4,2,2]
    result = findDisappearedNumbers(data)
    print(result)