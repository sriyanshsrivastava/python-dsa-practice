from Searching import ceiling

def floor(data:list[int], target: int)->int:
    start=0
    end = len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if target < data[mid]:
            end = mid-1
        elif target > data[mid]:
            start = mid + 1
        else:
            return mid
    return end


if __name__=="__main__":
    data = [2,3,5,9,14,16,18]
    target = 15

    print(floor(data,target))

    # printing ceiling value also

    print(ceiling(data,target))


