import time
def next_triangular_number(currTriNum,i):
    i+=1
    currTriNum += i
    return currTriNum,i
def get_triangular_number(numMaxFactor):
    currTriNum = 0
    i = 0
    currFactors = 0
    while currFactors < numMaxFactor:
        currFactors = 0
        currTriNum,i = next_triangular_number(currTriNum,i)
        sqrtTriNum = int(currTriNum**0.5)
        for k in range(1,sqrtTriNum):
            if currTriNum % k == 0:
                currFactors +=2
        if sqrtTriNum ** 2 == currTriNum:
            currFactors+=1
        #print(i,currFactors,currTriNum)
    return currTriNum
if __name__ == '__main__':
    start_time = time.clock()
    print(get_triangular_number(500))
    end_time = time.clock()
    print("Time Taken:",(end_time-start_time))
