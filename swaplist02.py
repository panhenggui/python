def swaplist(newlist):
    newlist[0],newlist[-1] = newlist[-1],newlist[0]
    return newlist

if __name__ == '__main__':
    newlist = [1,2,3,4]
    print(swaplist(newlist))