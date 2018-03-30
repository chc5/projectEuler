import math, time
def get_nth_prime(n):
    prime = [2]
    i = 1
    key = 3
    while i < n:
        for j in prime:
            if key % j == 0:
                break
        else:
            prime.append(key)
            i+=1
        key+=2
    return prime[i-1]
if __name__ == '__main__':
    start_time = time.time()
    print(get_nth_prime(10001))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
