def Reverse(lst):
    return [ele for ele in reversed(lst)]

if __name__ == '__main__':
    lst = [11,22,33,44,55]
    print(Reverse(lst))

def Reverse(lst):
    lst.reverse()

    return lst
if __name__ == '__main__':
    lst = [66,77,88,99,100]
    print(Reverse(lst))
    
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

if __name__ == '__main__':
    lst = [111,222,333,444,555]
    print(Reverse(lst))