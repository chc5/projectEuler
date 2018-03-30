import time
def sum_square_difference_of_first(n):
    squares_of_sum = 0
    for i in range(n+1):
        squares_of_sum+=i
    squares_of_sum = squares_of_sum**2
    sum_of_squares = 0
    for i in range(n+1):
        sum_of_squares+= i ** 2
    return squares_of_sum - sum_of_squares
if __name__ == '__main__':
    start_time = time.time()
    print(sum_square_difference_of_first(100))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
