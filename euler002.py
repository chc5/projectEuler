import time
def sum_of_even_fibon_less_than(num):
    memo = [1,1]
    sum = 0
    prev_fib = True # false is memo[0] and true is memo[1]
    while memo[0] < num and memo[1] < num:
        if prev_fib:
            memo[1] += memo[0]
            if memo[1] % 2 == 0:
                sum+= memo[1]
        else:
            memo[0] += memo[1]
            if memo[0] % 2 == 0:
                sum+= memo[0]
        prev_fib = not prev_fib
    return sum
if __name__ == '__main__':
    start_time = time.time()
    print(sum_of_even_fibon_less_than(4000000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
