def solve(num):
    fib_number_prev, fib_number_curr = 1, 1
    sum = 0
    while sum <= num:
        fib_number_temp = fib_number_curr
        fib_number_curr = fib_number_curr + fib_number_prev
        fib_number_prev = fib_number_temp
        if fib_number_curr % 2 == 0:
            sum += fib_number_curr
    return sum

if __name__ == '__main__':
    print(solve(4000000))
