import math
def largest_prime_factor(num):
    sqrtn = int(math.sqrt(num))
    i = 2
    largest_factor = 1
    while num % i == 0:
        num /= i
        largest_factor = i
    for i in range(3,sqrtn,2):
        while num % i == 0:
            num /= i
            largest_factor = i
    return largest_factor
if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
