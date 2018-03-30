import time
def get_multiples_of(factor1,factor2,num):
    sum = 0
    if factor2 < factor1:
        factor1, factor2 = factor2, factor1
    for i in range(factor1,num):
        if i % factor1 == 0 or i % factor2 == 0:
            sum += i
    return sum
if __name__ == '__main__':
    start_time = time.time()
    print(get_multiples_of(3,5,1000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
