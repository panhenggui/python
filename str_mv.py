def str_mv(test_str):
    print("原始字符串是："+ test_str)
    new_str = ""
    for i in range(len(test_str)):
        if i != 2:
            new_str += test_str[i]
    return new_str
if __name__ == '__main__':
    my_test_str = "Runoob"
    print("字符串移除后是：", str_mv(my_test_str))