#   There is 40 Choose 20 paths to get
#   to a point but I will be solving
#   it through memoization.
def iterativeLatticePaths(a,b):
    memo = [[0 for i in range(b+1)] for j in range(a+1)]
    for i in range(a+1):
        memo[i][0] = 1
    for j in range(b+1):
        memo[0][j] = 1
    for i in range(1,a+1):
        for j in range(1,b+1):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[a][b]
if __name__ == '__main__':
    print(iterativeLatticePaths(20,20))
