import time
class MaximumPathSum():
    def __init__(self,fileName):
        self.fileName = fileName
        self.path = []
        with open(fileName,"r") as f:
            self.path = f.read()
            self.path = [list(map(int,line.split(" "))) for line in self.path.split("\r\n")]
    def getSum(self):
        n = len(self.path) - 1
        while n > 0:
            for i in range(n-1,-1,-1):
                self.path[n-1][i] += max(self.path[n][i],self.path[n][i+1])
            n -= 1
        return self.path[0][0]
if __name__ == '__main__':
    start_time = time.time()
    fileName = "euler018_t.txt"
    m = MaximumPathSum(fileName)
    print(m.getSum())
    end_time = time.time()
    print("Time Taken:",end_time-start_time)
