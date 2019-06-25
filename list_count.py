def countX(lst,x):
    count = 0
    for ele in lst:
        if  (ele == x):
            count +=1

    return count
if __name__ == '__main__':
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    x = 8
    print(countX(lst,x))

def countX(lst,x):
    return lst.count(x)
if __name__ == '__main__':
    lst = [3,2,5,7,8,3,6,3]
    x = 3
    print(countX(lst,x))