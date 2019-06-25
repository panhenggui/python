def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在")
    else:
        print("存在")

if __name__ == '__main__':
    string = "www.runoob.com"
    sub_str = "runoob"
    sub_str2 = "hi"
    check(string,sub_str)
    check(string,sub_str2)