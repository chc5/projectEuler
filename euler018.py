import time
class MaximumPathSum():
    def __init__(self,file_name):
        self.file_name = file_name
        self.path = []
        with open(file_name,"r") as f:
            self.path = f.read().split("\n")
            self.path = [[int(i) for i in row.split()] for row in self.path]
    def getSum(self):
        n = len(self.path) - 1
        while n > 0:
            for i in range(n-1,-1,-1):
                self.path[n-1][i] += max(self.path[n][i],self.path[n][i+1])
            n -= 1
        return self.path[0][0]
if __name__ == '__main__':
    start_time = time.time()
    file_name = "euler018_t.txt"
    m = MaximumPathSum(file_name)
    print(m.getSum())
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
