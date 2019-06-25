def list_total(lst):
    total = 0
    for ele in range(len(lst)+1):
        total +=  ele

    return total

if __name__ == '__main__':
    lst = [1,2,3,4]
    print(list_total(lst))

def list_total(lst):
    total = 0
    ele = 0
    while (ele < len(lst)):
        total += lst[ele]
        ele += 1
    return total
if __name__ == '__main__':
    lst = [5,6,7,8]
    print(list_total(lst))

def sumOflist(list,size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOflist(list,size - 1)

if __name__ == '__main__':
    list = [10,20,30,40]
    total = sumOflist(list,len(list))
    print("列表元素之和是：" ,total)