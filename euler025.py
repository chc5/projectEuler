import math, time
def get_first_fibon_with_digits(max_digits):
    memo = [1,1]
    maxValue = 10**(max_digits-1)
    prev_fib = True # false is memo[0] and true is memo[1]
    counter = 2
    while memo[0] < maxValue and memo[1] < maxValue:
        if prev_fib:
            memo[1] += memo[0]
        else:
            memo[0] += memo[1]
        prev_fib = not prev_fib
        counter += 1
    return counter

if __name__ == '__main__':
    start_time = time.time()
    print(get_first_fibon_with_digits(1000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
