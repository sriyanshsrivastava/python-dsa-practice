"""
     Missing Number

    ** Previously asked in Amazon

    Given an array nums containing n distinct numbers in the range [0,n], return the only number
    in the range that is missing form the array.

    Follow Up: could you implement a solution using only O(1) extra space complexity and O(n)
    run time complexity?

    Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
        2 is the missing number in the range since it does not appear in nums.

    Link:https://leetcode.com/problems/missing-number/
"""
from typing import List

def missingVlaue(data:List[int])->int:
    i = 0
    while i < len(data):
        correct = data[i]
        if data[i]<len(data) and i!=correct:
            data[i],data[correct] = data[correct],data[i]
        else:
            i+=1

    for j in range(0,len(data)):
        if data[j]!=j:
            return j

    return len(data)


if __name__=="__main__":
    data=[0,2,1]
    answer = missingVlaue(data)
    print(answer)