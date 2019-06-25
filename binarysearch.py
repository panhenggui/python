def binarySearch(arr,l,r,x):
    if r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1

if __name__ == '__main__':
    arr = [3,12,23,34,41,55,63,89]
    result = binarySearch(arr,0,len(arr)-1,x=3)
    if result != -1:
        print("元素在数组中的索引是：\033[32;1m %d\033[0m" % result)
    else:
        print("\033[31;1m元素不在数组中\033[0m")