import time
def next_triangular_number(curr_tri_num,i):
    i+=1
    curr_tri_num += i
    return curr_tri_num,i
def get_triangular_number(max_factor):
    curr_tri_num = 0
    i = 0
    curr_factors = 0
    while curr_factors < max_factor:
        curr_factors = 0
        curr_tri_num,i = next_triangular_number(curr_tri_num,i)
        sqrt_tri_num = int(curr_tri_num**0.5)
        for k in range(1,sqrt_tri_num):
            if curr_tri_num % k == 0:
                curr_factors +=2
        if sqrt_tri_num ** 2 == curr_tri_num:
            curr_factors+=1
        #print(i,curr_factors,curr_tri_num)
    return curr_tri_num
if __name__ == '__main__':
    start_time = time.time()
    print(get_triangular_number(500))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
