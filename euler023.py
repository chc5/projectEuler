import time, euler021

def is_abundant(num):
    return num < euler021.divisor_sum(num)
def find_abundant_nums(num):
    abundant = []
    for i in range(12,num):
        if is_abundant(i):
            abundant.append(i)
    return abundant
def find_nonabundant_sums():
    n = 28124
    abundant_nums = find_abundant_nums(n)
    is_nonabundant_sums = [True for i in range(n)]
    nonabundant_sums = []
    for abundant1 in abundant_nums:
        for abundant2 in abundant_nums:
            total = abundant1 + abundant2
            if total < n:
                is_nonabundant_sums[total] = False
    for i in range(n):
        if not is_nonabundant_sums[i]:
            nonabundant_sums.append(i)
    return nonabundant_sums
if __name__ == '__main__':
    start_time = time.time()
    nonabundant = find_nonabundant_sums()
    print(sum(nonabundant))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
