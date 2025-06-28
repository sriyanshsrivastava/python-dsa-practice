from typing import List
from Sorting import getMaxIndex,swap


def selectionSort(data:List[int])->List[int]:
    sortedData = data.copy()
    for i in range(0, len(sortedData)):
        lastIndex = len(sortedData)-1-i
        maxIndex = getMaxIndex(sortedData,0,lastIndex)
        swap(sortedData,maxIndex,lastIndex)
    return sortedData


if __name__=="__main__":
    unsortedData =[1,50,3,80,5,6,70,10]
    print(unsortedData)
    sortedData = selectionSort(unsortedData)
    print(sortedData)
