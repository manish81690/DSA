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


def recursionBinarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    if arr[mid]>target:
        return recursionBinarySearch(arr,low,mid-1,target)
    else:
        return recursionBinarySearch(arr,mid+1,high,target)
arr=[1,2,3,4,5,6,7,8,9,11,14]
low=0
high=len(arr)-1
print(binarySearch(arr,low,high,3))
print(recursionBinarySearch(arr,low,high,3))