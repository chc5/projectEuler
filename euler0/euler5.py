import math
def smallest_multiple(n):
    list = [ int(i) for i in range(2,n+1) ]
    print(list)
    l = len(list)-1
    multiple = 1
    while l>=0:
        if multiple % list[l] != 0:
            temp = multiple
            while temp % 2 == 0 and list[l] % 2 == 0:
                list[l] /= 2
                temp /= 2
            for i in range(3,int(math.sqrt(multiple)),2):
                while list[l] % i == 0 and temp % i == 0:
                    list[l]/= i
                    temp/= i
            multiple *= list[l]
        del list[l]
        l-=1
    return int(multiple)
print(smallest_multiple(20))
