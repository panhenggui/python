def copy_list(li1):
    li_copy = li1[:]
    return li_copy

if __name__ == '__main__':
    li1 = [100,200,300,400]
    li2 = copy_list(li1)
    print("原始列表：",li1)
    print("复制列表：",li2)

def copy_list(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

if __name__ == '__main__':
    li1 = [500,600,700,800]
    li2 = copy_list(li1)
    print("原始列表：",li1)
    print("复制列表：",li2)

def copy_list(li1):
    li_copy = list(li1)
    return li_copy

if __name__ == '__main__':
    li1 = [103,203,303,403]
    li2 = copy_list(li1)
    print("原始列表：",li1)
    print("复制列表：",li2)