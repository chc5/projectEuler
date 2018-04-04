import time, euler021

def is_abundant(num):
    return num < euler021.divisor_sum(num)
def find_abundant_nums(low,high):
    abundant = []
    for i in range(low,high):
        if is_abundant(i):
            abundant.append(i)
    return abundant
def find_nonabundant_sums(n):
    abundant_nums = find_abundant_nums(1,n)
    size = len(abundant_nums)
    is_nonabundant_sums = [True for i in range(n)]
    nonabundant_sums = []
    for i in range(size):
        for j in range(i,size):
            total = abundant_nums[i] + abundant_nums[j]
            if total < n:
                is_nonabundant_sums[total] = False
            else:
                break
    for i in range(n):
        if is_nonabundant_sums[i]:
            nonabundant_sums.append(i)
    return nonabundant_sums
if __name__ == '__main__':
    start_time = time.time()
    nonabundant = find_nonabundant_sums(28124)
    print(sum(nonabundant))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
