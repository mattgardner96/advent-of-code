import os
from re import finditer

os.chdir("/Users/mattgardner/Documents/advent-of-code/day3")

# read in the input
lines = open("input.txt","r").readlines()

# create a list to store numbers and positions
nums_array = list()

def part1():
    find_numbers(lines,nums_array)
    return pn_checker(lines,nums_array)

# find every number's position in the matrix
def find_numbers(lines,nums_array):
    for line_num,this_line in enumerate(lines):
        for match in finditer(r'\d+', this_line):
            nums_array.append([line_num, match.group(), match.span(), False])   # legend: [line_num, matched number, span, is_pn:default False]

# pn checker (the hard part)
def pn_checker(lines,nums_array):

    sum_parts = 0;
    
    # check adjacent characters surrounding the number (do this first on same line, then above, then below)
    for num in nums_array:
        line_number = num[0]
        curr_line = lines[line_number]
        start_char_num = num[2][0]-1
        end_char_num = num[2][1]

        # check same line; if it's on the end of the line, assume char before or after is a period and we don't care about it
        before_char = curr_line[start_char_num] if num[2][0] >= 1 else '.'; # print("number",num[1],"before_char",before_char)
        after_char = curr_line[end_char_num] if end_char_num < len(curr_line) else '.';  # print("number",num[1],"after_char",after_char)
        if before_char != '.' or after_char != '.':
            num[3] = True # set is_pn True

        # check above line
        if line_number > 0:
            checkstring_top = '0'
            if start_char_num > 0 and end_char_num < len(lines[line_number-1])-1:     # middle of a line
                checkstring_top = (lines[line_number-1][start_char_num:end_char_num+1])
            if start_char_num == 0 and end_char_num < len(lines[line_number-1])-1:    # start of a line
                checkstring_top = (lines[line_number-1][start_char_num+1:end_char_num+1])
            if start_char_num > 0 and end_char_num == len(lines[line_number-1])-1:    # end of a line
                checkstring_top = (lines[line_number-1][start_char_num:end_char_num])
                print(checkstring_top)                                                # NEVER EXECUTES
            
            # return True if checkstring contains something other than a period or a number
            if any(char not in '.0123456789' for char in checkstring_top):
                num[3] = True


        # check below line
        if line_number < len(lines)-1:
            checkstring_bottom = '0'
            if start_char_num > 0 and end_char_num < len(lines[line_number+1])-1:     # middle of a line
                checkstring_bottom = (lines[line_number+1][start_char_num:end_char_num+1])
            if start_char_num == 0 and end_char_num < len(lines[line_number+1])-1:    # start of a line
                checkstring_bottom = (lines[line_number+1][start_char_num+1:end_char_num+1])
            if start_char_num > 0 and end_char_num == len(lines[line_number+1])-1:    # end of a line
                checkstring_bottom = (lines[line_number+1][start_char_num:end_char_num])
                print(num[1])
                print(checkstring_bottom)                                             # NEVER EXECUTES
            # return True if checkstring contains something other than a period or a number
            if any(char not in '.0123456789' for char in checkstring_bottom):
                print(char not in '.0123456789' for char in checkstring_bottom)
                num[3] = True

        if num[3] == True:
            sum_parts += int(num[1])

        if num[2][1] == len(curr_line)-1:
            pass
            # print(num[0]+1,num[1],"is_pn",num[3],sep='\t')

    return sum_parts




if __name__ == "__main__":
    print(part1())
    # print(nums_array) print("line",nums_array[-1][0],"number",nums_array[-1][1],"start+end",nums_array[-1][2],"is_pn",nums_array[-1][3])   # DEBUG