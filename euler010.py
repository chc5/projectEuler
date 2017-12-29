import math
# Sieve of Eratosthenes
def sum_of_primes(n):
    primes = [True for i in range(0,n)]
    for i in range(2,int(math.sqrt(n))):
        if primes[i] == True:
            for j in range(i*i,n,i):
                primes[j] = False
    sumOfPrimes = 0
    for i in range(2,n):
        if primes[i] == True:
            sumOfPrimes+=i
    return sumOfPrimes
if __name__ == '__main__':
    print(sum_of_primes(2000000))
