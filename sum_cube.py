def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i**3

    return sum

if __name__ == '__main__':
    n = int(input("输入要计算立方和的数："))
    print(sumOfSeries(n))