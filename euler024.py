import time
def factorial(n):
    product = 1
    i = 2
    while i <= n:
        product *= i
        i += 1
    return product
def N_th_permutation(arr,n):
    size = len(arr) - 1
    n -= 1
    permutation = []
    while size > 0:
        arr.sort()
        counter = 0
        combination = factorial(size)
        while combination <= n:
            n -= combination
            counter += 1
        permutation.append(arr[counter])
        arr.remove(arr[counter])
        size -= 1
    permutation.append(arr[0])
    arr.remove(arr[0])
    for i in range(len(permutation)):
        arr.append(permutation[i])
def next_lexicographic_permutation(arr):
    size = len(arr)
    i,j = 0,0
    for i in range(size-1,0,-1):
        if arr[i - 1] < arr[i]:
            break
    for j in range(size-1,0,-1):
        if arr[j] > arr[i-1]:
            break
    arr[i - 1], arr[j] = arr[j], arr[i-1]
    arr[i: ] = arr[size-1: i-1 :-1]
if __name__ == '__main__':
    start_time = time.time()
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    N_th_permutation(arr,1000000)
    print(arr)
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
