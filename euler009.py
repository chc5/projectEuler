import math, time
#   Constructing Pythagorean Triples
#   involves the following equations:
#   a = n^2-m^2
#   b = 2nm
#   c = n^2+m^2
#   sum = a+b+c = n^2 +n^2 -m^2 + m^2 + 2nm
#   sum = 2n^2 + 2nm
#   where m < n
def get_pythag_triplets(total):
#   Assume that m = 1
#   a = n^2 - 1
#   b = 2n(1)
#   c = n^2 + 1
#   sum = a+b+c = n^2 - 1 + 2n + n^2 + 1
#   sum = 2n^2 + 2n
#   sum/2 = n^2 + n
#   sum/2 + 1/4 = n^2 + n + 1/4
#   sum/2 + 1/4 = (n+1/2)^2
#   +sqrt(sum/2 + 1/4) = n+1/2
#   n = -1/2 + sqrt(sum/2+1/4)
    n = int(-0.5+math.sqrt((total/2)+0.25))
    for i in range(1,n+1): # sum = 2n^2 + 2nm
        x = 2*(i**2)
        f = 2*i # Factor of y
        y = 0
        for j in range(1,i):
            y += f
            if total % (x+y) == 0:
                factor = total / (x+y)
                squared_n = i**2
                squared_m = j**2
                a = factor*(squared_n - squared_m)
                b = factor*2*i*j
                c = factor*(squared_n+squared_m)
                return a,b,c,factor
    return -1,-1,-1
if __name__ == '__main__':
    start_time = time.time()
    a,b,c,factor = get_pythag_triplets(1000)
    print(int(a*b*c))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
