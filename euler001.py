import time
def isMultiOf3And5(num):
    return num % 3 == 0 or num % 5 == 0
def sumOfMultiOf3And5(num):
    sum = 0
    for i in range(3,num):
        if isMultiOf3And5(i):
            sum+=i
    return sum
if __name__ == '__main__':
    start_time = time.time()
    print(sumOfMultiOf3And5(1000))
    end_time = time.time()
    print("Time Taken:",end_time-start_time)
