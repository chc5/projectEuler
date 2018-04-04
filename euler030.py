import time
def is_power_same_as_(n,exp,powers):
    powerSum = 0
    temp = n
    while temp > 0:
        powerSum += powers[temp % 10]
        temp = temp // 10
    return powerSum == n
def digit_fifth_powers(exp):
    powers = [int(i)**exp for i in range(10)]
    powers_same = []
    for i in range(2,10**(exp+1)):
        if is_power_same_as_(i,exp,powers):
            powers_same.append(i)
    return powers_same
if __name__ == '__main__':
    start_time = time.time()
    print(sum(digit_fifth_powers(5)))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
