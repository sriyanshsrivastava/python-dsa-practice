# Binary search algorithm code and implementation

def binarySearch(data:list[int],target:int)->int:
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if target < data[mid]:
            end = mid - 1
        elif target > data[mid]:
            start = mid + 1
        else:
            return mid

    return -1


if __name__=="__main__":
    data = [1,2,8,6,7,12,89,100,102,120,148,150]
    target = 99

    print(binarySearch(data,target))