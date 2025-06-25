"""
     Find first and Last position of element in Sorted array.

    Given an array of integers nums sorted in ascending order, find the starting and ending position of
    given target value.

    if target is not found in array , return [-1,-1]
    You must write an algorithm with O(logN) runtime complexity.

    Example:
          Input: nums = [5,7,7,8,8,10], Target = 8
          output: [3,4]

    Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""

def searchRange(data:list[int],target:int)->list[int]:
    answer = [-1,-1]
    answer[0]=search(data,target,True)
    answer[1]=search(data,target,False)
    return answer

def search(data:list[int],target:int,findFirstOccurrenceIndex:bool)->int:
    answer = -1
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if target < data[mid]:
            end = mid - 1
        elif target > data[mid]:
            start = mid + 1
        else:
            answer = mid
            if findFirstOccurrenceIndex:
                end = mid - 1
            else:
                start = mid + 1

    return answer

# Driver code this will run as main()
if __name__=="__main__":
    data = [5,7,7,7,7,7,8,8,10]
    target = 15

    print(searchRange(data,target))