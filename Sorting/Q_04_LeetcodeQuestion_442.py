"""
    Find all Duplicates in Array

    Given an integer array nums of length n where all integers of nums are
    in rhe range [1,n] and each integer appears once or twice, return an array
    of all the integers that appears twice.

    you must write an algorithm that runs in O(n) time and uses only constant
    extra space.

    Example:
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [2,3]

    Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""
from typing import List

from django.db.models.expressions import result

from UtilityTools import swap

def findDuplicates(data: List[int])->List[int]:
    i = 0
    while i< len(data):
        correct = data[i]-1
        if data[i]!=data[correct]:
            swap(data,i, correct)
        else:
            i+=1

    result = []
    for j in range (0, len(data)):
        if data[j]!=j+1:
            result.append(data[j])

    return  result


if __name__=="__main__":
    data = [4,3,2,7,8,2,3,1]
    result = findDuplicates(data)
    print(result)
