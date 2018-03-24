import time
def power_digit_sum(n,e):
    num = n**e
    string = str(num)
    sum_of_digits = 0
    for key in string:
        if key != '0':
            sum_of_digits += int(key)
    return sum_of_digits
if __name__ == '__main__':
    start_time = time.clock()
    print(power_digit_sum(2,1000))
    end_time = time.clock()
    print("Time Taken:",end_time-start_time)
