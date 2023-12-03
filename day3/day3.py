import os
from re import finditer

os.chdir("/Users/mattgardner/Documents/advent-of-code/day3")

# read in the input
lines = open("test.txt","r").readlines()

# create a list to store numbers and positions
nums_array = list()

# find every number's position in the matrix
def find_numbers(lines,nums_array):
    for line_num,this_line in enumerate(lines):
        for match in finditer(r'\d+', this_line):
            nums_array.append([line_num, match.group(), match.span(), False])   # legend: [line_num, matched number, span, is_pn:default False]
            print("line",nums_array[-1][0],"number",nums_array[-1][1],"start+end",nums_array[-1][2],"is_pn",nums_array[-1][3])   # DEBUG

# pn checker (the hard part)
def pn_checker(lines,nums_array):
    pass
    for i,this_number in enumerate(nums_array):
        # check adjacent characters surrounding the number (do this first on same line, then above, then below)
        
        # check same line
        before_char = lines[this_number[0]][this_number[2][0]-1] if this_number[2][0] > 0 else None
        after_char = lines[this_number[0]][this_number[2][1]] if this_number[2][1] < len(lines[this_number[0]]) else None
        print("line_num",i,"before_char",before_char,"after_char",after_char)


if __name__ == "__main__":
    find_numbers(lines,nums_array)
    pn_checker(lines,nums_array)    
