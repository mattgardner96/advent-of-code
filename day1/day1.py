
import re
import fileinput

# lines = list(fileinput.input())
lines = open("day1.txt", "r").readlines()

def countup(curr_sum,first_digit,last_digit):
    return curr_sum + first_digit * 10 + last_digit


# create function for part 1
def part1(lines):
    sum = 0
    # for each line in the array
    for line in lines:

        # find the first digit in the line
        for i, c in enumerate(line):
            if c.isdigit():
                first_digit = int(c)
                break
        
        # find the last digit in the line
        last_digit = re.findall(r'\d{1}', line)[-1]

        sum = countup(sum,first_digit,int(last_digit))
    
    return(sum)

def part2(lines):
    # create dictionary of ten digits as words
    digits = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
    }

    sum = 0
    # for each line in the array
    for line in lines:

        # problem: ends when the first key in the dictionary is found, but the first digit is not the first key in the dictionary
        first_word_index = 100

        for key in digits:
            if key in line:
                if line.index(key) < first_word_index:
                    first_word = digits[key]
                    first_word_index = line.index(key)
                    
        # find the first number digit in the line
        for i, c in enumerate(line):
            if c.isdigit():
                first_num = int(c)
                first_num_index = i
                break

        # ternary operator
        first_digit = first_word if first_word_index <= first_num_index else first_num
        # print("line, first_digit", line.strip(), first_digit)
        
        # find the last number digit in the line
        try: 
            last_num = re.findall(r'\d{1}', line)[-1]
            last_num_index = line.rindex(last_num)
        except IndexError:
            last_num = "None"
            last_num_index = -1

        # find the last instance of a key in digits in the string

        last_word_index = -1
        for key in digits:
            if key in line:
                if line.rindex(key) > last_word_index:
                    last_word = digits[key]
                    last_word_index = line.rindex(key)
        
        # ternary
        last_digit = last_num if last_num_index > last_word_index else last_word
        # print("     last_digit: ", last_digit)

        sum = countup(sum,first_digit,int(last_digit))
    
    # print(lines)
    return(sum)

if __name__ == "__main__":
    # print(part1(lines))

    print(part2(lines))
    
    pass