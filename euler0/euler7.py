import math
def getNthPrime(n):
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
print(getNthPrime(10001))
