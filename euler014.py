import time
class CollatzChains():
    def __init__(self):
        self.chains = dict()
        self.chains[1] = 1
    def link(self,num):
        if num % 2 == 0:
            return int(num/2)
        else:
            return int(3*num+1)
    def get_collatz_length(self,num):
        if num in self.chains:
            return self.chains[num]
        else:
            count = 1 + self.get_collatz_length(self.link(num))
            self.chains[num] = count
            return count
    def longest_collatz(self,n):
        max_chain = 0
        max_length = 0
        chains = dict()
        for i in range(1,n):
            count = self.get_collatz_length(i)
            if max_length < count:
                max_chain = i
                max_length = count
        return max_chain
if __name__ == '__main__':
    start_time = time.time()
    test = CollatzChains()
    print(test.longest_collatz(1000000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
