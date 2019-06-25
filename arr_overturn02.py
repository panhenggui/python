def leftRotate(arr, d, n):
    for i in range(gcd(d, n)):
        temp =arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i],end=" ")

def gcd(a,b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    leftRotate(arr,6,8)
    printArray(arr, 8)