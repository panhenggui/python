from bisect import bisect_left

test_list = [1,6,3,5,3,4,5]
print("查看4是否在列表中（使用循环）：")
for i in test_list:
    if (i == 4):
        print("存在")

print("查看4是否存在（使用in关键字）：")
if (4 in test_list):
    print("存在")

print("查看4是否在列表中（使用set() + in):")
test_list = set(test_list)
if 4 in test_list:
    print("存在")

print("查看4是否在列表中（使用sort() + bisect_left()）:")
test_list.sort()
if bisect_left(test_list,4):
    print("存在")