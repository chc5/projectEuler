if __name__  == '__main__':
    with open("euler013_t.txt","r") as f:
        data = f.read().split()
        data = [int(i) for i in data]
        sumdata = sum(data)
        print(str(sumdata)[0:10])
