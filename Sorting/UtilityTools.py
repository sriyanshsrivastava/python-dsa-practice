from typing import List

# function to swap two value in given array
def swap(data:List[int],firstValue:int,secondValue:int):
    data[firstValue],data[secondValue] = data[secondValue],data[firstValue]

# returns the maximum value index.
def getMaxIndex(data:List[int],start:int,end:int)->int:
    maxValue = data[start]
    maxIndex = start
    for i in range(start,end+1):
        if data[i] >= maxValue:
            maxValue = data[i]
            maxIndex = i
    return maxIndex

if __name__=="__main__":
    data=[1,2,3,4,5,6,70,10]
    swap(data,0,1)
    print(data)
    print(getMaxIndex(data,0, len(data)-1))