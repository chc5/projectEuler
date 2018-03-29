import time
# Goal is to remove all the 5s and 10s and 2s from the number itself
# because they produce 0s in the digit sum
# I'm doing this to reduce the amount of multiplications it takes to get digit sums.
# Time saved: 100 % - 0.00033020973205566406 / 0.0007331371307373047 * 100 % = 55 %
def factorial_digit_sum(num):
    factorial = 1
    for i in range(1,num+1):
        if i % 5 == 0 and i % 10 == 2:
            continue
        factorial *= i
    digit_sum = 0
    while factorial > 0:
        digit_sum += factorial % 10
        factorial = factorial // 10
    return digit_sum
if __name__ == '__main__':
    start_time = time.time()
    print(factorial_digit_sum(100))
    end_time = time.time()
    print("Time Taken:",end_time-start_time)
