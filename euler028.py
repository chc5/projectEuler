import time
def getSumOfCorners(n):
    top_right = n**2
    top_left = top_right - n + 1
    bottom_left = top_left - n + 1
    bottom_right = bottom_left - n + 1
    return top_right + top_left + bottom_left + bottom_right
def number_spiral_diagonals(n):
    count = 1
    spirals = 1
    while spirals < n:
        spirals += 2
        count += getSumOfCorners(spirals)
    return count
if __name__ == '__main__':
    start_time = time.time()
    print(number_spiral_diagonals(1001))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
