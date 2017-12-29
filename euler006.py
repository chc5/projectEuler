def getSumSquareDifference(n):
    squaresOfSum = 0
    for i in range(n+1):
        squaresOfSum+=i
    squaresOfSum = squaresOfSum**2
    sumOfSquares = 0
    for i in range(n+1):
        sumOfSquares+= i ** 2
    return squaresOfSum - sumOfSquares
if __name__ == '__main__':
    print(getSumSquareDifference(100))
