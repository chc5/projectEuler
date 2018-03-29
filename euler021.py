import time, math
def getSumOfDivisor(num):
    sqrtNum = int(math.sqrt(num))
    # print(num,sqrtNum)
    total = 1
    for i in range(2,sqrtNum+1):
        if num % i == 0:
            total += i + num // i
            # if num == 220:
            #     print(i, num // i)
    # print(sqrtNum)
    if sqrtNum*sqrtNum == num:
        total -= sqrtNum
    return total
def getAmicablePartner(num):
    partner = getSumOfDivisor(num)
    realNum = getSumOfDivisor(partner)
    # if(num == 284):
    #     print(num,partner,realNum)
    if realNum == num and num != partner:
        return partner
    return None
def getSumOfAmicableNums(length):
    amicableNums = [False for i in range(length+1)]
    total = 0
    for i in range(2,length+1):
        if amicableNums[i] == False:
            partner = getAmicablePartner(i)
            if partner != None:
                if partner < length + 1:
                    amicableNums[partner] = True
                total += i
        else:
            total += i
    return total
if __name__ == '__main__':
    start_time = time.time()
    print(getSumOfAmicableNums(10000))
    end_time = time.time()
    print("Time Taken:",end_time-start_time)
