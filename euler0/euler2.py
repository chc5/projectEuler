def getEvenFibonacci(num):
    memo = [1,1]
    sum = 0
    prevFib = True # false is memo[0] and true is memo[1]
    for i in range(num):
        if prevFib:
            memo[1] += memo[0]
            if memo[1] % 2 == 0:
                sum+= memo[1]
        else:
            memo[0] += memo[1]
            if memo[0] % 2 == 0:
                sum+= memo[0]
        prevFib = not prevFib
    return sum
print(getEvenFibonacci(31))
