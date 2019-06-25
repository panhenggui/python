def findLen(str):
    counter = 0
    while str[counter:]:
        counter +=1
    return counter

if __name__ == '__main__':
    str = "runoob"
    print(findLen(str))
    print(len(str))