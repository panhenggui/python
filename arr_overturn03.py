def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr,0,d-1)
    rverseArray(arr,d,n-1)
    rverseArray(arr,0,n-1)

def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=" ")

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    leftRotate(arr,7)
    printArray(arr)
