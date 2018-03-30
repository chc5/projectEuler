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
        self.letter_counts = dict()
        self.letter_counts[0] = len("")
        self.letter_counts[1] = len("one")
        self.letter_counts[2] = len("two")
        self.letter_counts[3] = len("three")
        self.letter_counts[4] = len("four")
        self.letter_counts[5] = len("five")
        self.letter_counts[6] = len("six")
        self.letter_counts[7] = len("seven")
        self.letter_counts[8] = len("eight")
        self.letter_counts[9] = len("nine")
        self.letter_counts[10] = len("ten")
        self.letter_counts[11] = len("eleven")
        self.letter_counts[12] = len("twelve")
        self.letter_counts[13] = len("thirteen")
        self.letter_counts[14] = len("fourteen")
        self.letter_counts[15] = len("fifteen")
        self.letter_counts[16] = len("sixteen")
        self.letter_counts[17] = len("seventeen")
        self.letter_counts[18] = len("eighteen")
        self.letter_counts[19] = len("nineteen")
        self.letter_counts[20] = len("twenty")
        self.letter_counts[30] = len("thirty")
        self.letter_counts[40] = len("forty")
        self.letter_counts[50] = len("fifty")
        self.letter_counts[60] = len("sixty")
        self.letter_counts[70] = len("seventy")
        self.letter_counts[80] = len("eighty")
        self.letter_counts[90] = len("ninety")
        self.letter_counts[100] = len("hundred")
        self.letter_counts[1000] = len("thousand")
        self.And = len("and")
    def number_letter_counts(self,start,end):
        count = 0
        for i in range(start,end+1):
            double_digits = i % 100
            single_digit = double_digits % 10
            if double_digits <= 20:
                count += self.letter_counts[double_digits]
            else:
                count += self.letter_counts[(double_digits // 10) * 10] + self.letter_counts[single_digit]
            triple_digits = i % 1000
            third_digit = triple_digits // 100
            if third_digit > 0:
                count += self.letter_counts[third_digit] + self.letter_counts[100]
                if single_digit > 0 or double_digits > 0:
                    count += self.And
            quad_digits = i % 10000
            fourth_digit = quad_digits // 1000
            if fourth_digit > 0:
                count += self.letter_counts[fourth_digit] + self.letter_counts[1000]
        return count
if __name__ == '__main__':
    start_time = time.time()
    c = NumberToLetter()
    print(c.number_letter_counts(1,1000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
