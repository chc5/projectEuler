import math, time
# Sieve of Eratosthenes
def sum_of_primes(n):
    primes = [True for i in range(0,n)]
    for i in range(2,int(math.sqrt(n))):
        if primes[i] == True:
            for j in range(i*i,n,i):
                primes[j] = False
    sum_of_primes = 0
    for i in range(2,n):
        if primes[i] == True:
            sum_of_primes+=i
    return sum_of_primes
if __name__ == '__main__':
    start_time = time.time()
    print(sum_of_primes(2000000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
