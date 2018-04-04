import time
def coin_sums(coins,val,lastIndex):
    # print(val,size)
    if val == 0:
        return 1
    elif val < 0:
        return 0
    else:
        total = 0
        for i in range(lastIndex, -1, -1):
            maxCoins = val // coins[i]
            for j in range(1,maxCoins+1):
                total += coin_sums(coins, val - j * coins[i], i-1)
        return total
if __name__ == '__main__':
    start_time = time.time()
    # currency = [1, 2, 5]
    currency = [1, 2, 5, 10, 20, 50, 100, 200]
    print(coin_sums(currency, 200, len(currency)-1))
    # print(currency)
    # print(coin_sums(currency,7,len(currency)))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
