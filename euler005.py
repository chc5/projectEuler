import math, time
def smallest_multiple(n):
    factors = [ int(i) for i in range(2,n+1) ]
    print(list)
    curr_index = len(factors)-1
    multiple = 1
    while curr_index >= 0:
        if multiple % factors[curr_index] != 0:
            temp = multiple
            while temp % 2 == 0 and factors[curr_index] % 2 == 0:
                factors[curr_index] /= 2
                temp /= 2
            for i in range(3,int(math.sqrt(multiple)),2):
                while factors[curr_index] % i == 0 and temp % i == 0:
                    factors[curr_index] /= i
                    temp /= i
            multiple *= factors[curr_index]
        del factors[curr_index]
        curr_index -= 1
    return int(multiple)
if __name__ == '__main__':
    start_time = time.time()
    print(smallest_multiple(20))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
