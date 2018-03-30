import time, math
def divisor_sum(num):
    sqrt_num = int(math.sqrt(num))
    # print(num,sqrt_num)
    total = 1
    for i in range(2,sqrt_num+1):
        if num % i == 0:
            total += i + num // i
            # if num == 220:
            #     print(i, num // i)
    # print(sqrt_num)
    if sqrt_num * sqrt_num == num:
        total -= sqrt_num
    return total
def amicable_partner(num):
    partner = divisor_sum(num)
    realNum = divisor_sum(partner)
    # if(num == 284):
    #     print(num,partner,realNum)
    if realNum == num and num != partner:
        return partner
    return None
def amicable_nums_sum(length):
    amicable_nums = [False for i in range(length+1)]
    total = 0
    for i in range(2,length+1):
        if amicable_nums[i] == False:
            partner = amicable_partner(i)
            if partner != None:
                if partner < length + 1:
                    amicable_nums[partner] = True
                total += i
        else:
            total += i
    return total
if __name__ == '__main__':
    start_time = time.time()
    print(amicable_nums_sum(10000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
