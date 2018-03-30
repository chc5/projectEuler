import time
def generate_alphabet():
    alphabet = dict()
    for i in range(26):
        alphabet[chr(ord('A')+i)] = i+1
    return alphabet
def name_scores(name,alphabet,rank):
    total = 0
    for ch in name:
        total += alphabet[ch]
    return total*rank
def name_scores_sum(names,alphabet):
    total = 0
    n = len(names)
    for i in range(n):
        total += name_scores(names[i],alphabet,i+1)
    return total
def trim_quotes(str):
    return str[1:len(str)-2]
def read_file(fileName):
    with open(fileName,"r") as f:
        string = f.read()
        arr = [name[1:len(name)-1] for name in string.split(",")]
    return arr
if __name__ == '__main__':
    start_time = time.time()
    names = read_file("p022_names.txt")
    names.sort()
    alphabet = generate_alphabet()
    print(name_scores_sum(names,alphabet))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
