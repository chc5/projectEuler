def is_palindrome(num):
    string = str(num)
    l = len(string)
    j = l-1
    for i in range(int(l/2)):
        if string[i] != string[j]:
            return False
        j-=1
    return True
def find_largest_palindrome_2(minNum,num1,num2,maxNum):
    while num1 >= minNum and maxNum >= num2:
        num = num1*num2
        if is_palindrome(num):
            return num
        num1-=1
        num2+=1
    return -1
def find_largest_palindrome(minNum,maxNum):
    for i in range(maxNum,minNum-1,-1):
        num = find_largest_palindrome_2(minNum,i,i,maxNum)
        if num > 0:
            return num
    return "not found"
def get_largest_palindrome(digits):
    minNum = 10**(digits-1)
    maxNum = (10**digits)-1
    return find_largest_palindrome(minNum,maxNum)
print(get_largest_palindrome(8))
