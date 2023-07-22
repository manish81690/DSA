def binarySearch(arr,low,high,target):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1


def repetitionBinarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    if arr[mid]>target:
        return repetitionBinarySearch(arr,low,mid-1,target)
    else:
        return repetitionBinarySearch(arr,mid+1,high,target)
arr=[1,2,3,4,5,6,7,8,9,11,14]
low=0
high=len(arr)-1
print(binarySearch(arr,low,high,3))
print(repetitionBinarySearch(arr,low,high,3))