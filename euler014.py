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
    def getCollatzLength(self,num):
        if num in self.chains:
            return self.chains[num]
        else:
            count = 1 + self.getCollatzLength(self.link(num))
            self.chains[num] = count
            return count
    def longest_collatz(self,n):
        max_chain = 0
        max_length = 0
        chains = dict()
        for i in range(1,n):
            count = self.getCollatzLength(i)
            if max_length < count:
                max_chain = i
                max_length = count
        return max_chain
if __name__ == '__main__':
    start_time = time.clock()
    test = CollatzChains()
    print(test.longest_collatz(1000000))
    end_time = time.clock()
    print("Time taken:",end_time-start_time)
