import time
if __name__  == '__main__':
    start_time = time.time()
    with open("euler013_t.txt","r") as f:
        data = f.read().split()
        data = [int(i) for i in data]
        sumdata = sum(data)
        print(str(sumdata)[0:10])
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
