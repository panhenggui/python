def swaplist(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

if __name__ == '__main__':
    newlist = [1,2,3,4]
    print(swaplist(newlist))