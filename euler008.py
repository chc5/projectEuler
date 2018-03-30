import time
def build_memo(s,size,n,i):
    memo = []
    length = 0
    product = 1
    while length < n and i < size:
        key = int(s[i])
        i+=1
        if key == 0:
            length = 0
            memo = []
        else:
            memo.append(key)
            length+=1
    if length < n and i >= size:
        product = 0
    else:
        for m in memo:
            product*=m
    return memo,product,i
def largest_product_in_series(s,n): #O(n) operation
    size = len(s)
    max_product = 0
    counter = 0
    i = 0
    memo,product,i = build_memo(s,size,n,i)
    while i < size:
        if max_product < product:
            max_product = product
        product /= memo[counter]
        memo[counter] = int(s[i])
        product *= memo[counter]
        i+=1
        if product == 0:
            counter = 0
            memo,product,i = build_memo(s,size,n,i)
        else:
            counter = (counter+1)%n
    if max_product < product:
        max_product = product
    return int(max_product)
if __name__ == '__main__':
    start_time = time.time()
    with open("euler008_t.txt","r") as f:
        string = f.read()
    print(largest_product_in_series(string,13))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
