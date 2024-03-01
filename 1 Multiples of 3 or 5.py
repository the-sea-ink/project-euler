def solve():
    sum = 0
    for i in range(1, 1000):
        sum = sum + i if (i % 3 == 0 or i % 5 == 0) else sum
    return sum


if __name__ == '__main__':
    print(solve())
