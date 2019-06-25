def swapPositions(list, pos1, pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

if __name__ == '__main__':
    list = [11,22,33,44]
    pos1,pos2 = 1,3
    print(swapPositions(list,pos1-1, pos2-1))

def swapPositions(list,pos1,pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    list.insert(pos1,second_ele)
    list.insert(pos2,first_ele)

    return list

if __name__ == '__main__':
    list = [55,66,77,88]
    pos1,pos2 = 1,3

    print(swapPositions(list,pos1,pos2))

def swapPositions(list,pos1,pos2):
    get = list[pos1],list[pos2]
    list[pos2],list[pos1] = get

    return list

if __name__ == '__main__':
    list = [111,222,333,444]
    pos1,pos2 = 1,3
    print(swapPositions(list,pos2-1,pos1-1))