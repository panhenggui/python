def swaplist(newlist):
    get = newlist[-1],newlist[0]
    newlist[0],newlist[-1] = get

    return newlist

if __name__ == '__main__':
    newlist = [1,2,3,4]
    print(swaplist(newlist))