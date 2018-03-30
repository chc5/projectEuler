import math, time
def largest_prime_factor(num):
    sqrt_n = int(math.sqrt(num))
    i = 2
    largest_factor = 1
    while num % i == 0:
        num /= i
        largest_factor = i
    for i in range(3,sqrt_n,2):
        while num % i == 0:
            num /= i
            largest_factor = i
    return largest_factor
if __name__ == '__main__':
    start_time = time.time()
    print(largest_prime_factor(600851475143))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
