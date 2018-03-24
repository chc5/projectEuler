# Letter Counts from 1 to 9 is 3+3+5+4+4+3+5+5+4 = 36
# Letter Count of 10 is 3
# Letter Counts from 11 to 19 is 6+6+8+8+7+7+9+8+8 = 67
# Letter Counts of 20 to 90 in increments of 10 is 6+6+5+5+5+7+6+6 = 46
# Letter Counts of hundred is 7
# Letter Counts of and is 3
# Letter Counts of thousand is 8
import time
class NumberToLetter():
    def __init__(self):
        self.letterCounts = dict()
        self.letterCounts[0] = len("")
        self.letterCounts[1] = len("one")
        self.letterCounts[2] = len("two")
        self.letterCounts[3] = len("three")
        self.letterCounts[4] = len("four")
        self.letterCounts[5] = len("five")
        self.letterCounts[6] = len("six")
        self.letterCounts[7] = len("seven")
        self.letterCounts[8] = len("eight")
        self.letterCounts[9] = len("nine")
        self.letterCounts[10] = len("ten")
        self.letterCounts[11] = len("eleven")
        self.letterCounts[12] = len("twelve")
        self.letterCounts[13] = len("thirteen")
        self.letterCounts[14] = len("fourteen")
        self.letterCounts[15] = len("fifteen")
        self.letterCounts[16] = len("sixteen")
        self.letterCounts[17] = len("seventeen")
        self.letterCounts[18] = len("eighteen")
        self.letterCounts[19] = len("nineteen")
        self.letterCounts[20] = len("twenty")
        self.letterCounts[30] = len("thirty")
        self.letterCounts[40] = len("forty")
        self.letterCounts[50] = len("fifty")
        self.letterCounts[60] = len("sixty")
        self.letterCounts[70] = len("seventy")
        self.letterCounts[80] = len("eighty")
        self.letterCounts[90] = len("ninety")
        self.letterCounts[100] = len("hundred")
        self.letterCounts[1000] = len("thousand")
        self.And = len("and")
    def number_letter_counts(self,start,end):
        count = 0
        for i in range(start,end+1):
            doubledigits = i % 100
            singledigit = doubledigits % 10
            if doubledigits <= 20:
                count += self.letterCounts[doubledigits]
            else:
                count += self.letterCounts[(doubledigits // 10) * 10] + self.letterCounts[singledigit]
            tripledigits = i % 1000
            thirddigit = tripledigits // 100
            if thirddigit > 0:
                count += self.letterCounts[thirddigit] + self.letterCounts[100]
                if singledigit > 0 or doubledigits > 0:
                    count += self.And
            quaddigits = i % 10000
            fourthdigit = quaddigits // 1000
            if fourthdigit > 0:
                count += self.letterCounts[fourthdigit] + self.letterCounts[1000]
        return count
if __name__ == '__main__':
    start_time = time.clock()
    c = NumberToLetter()
    print(c.number_letter_counts(1,1000))
    end_time = time.clock()
    print("Time Taken:",end_time-start_time)
