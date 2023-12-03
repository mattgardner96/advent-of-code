import os
from re import finditer

os.chdir("/Users/mattgardner/Documents/advent-of-code/day3")

# read in the input
lines = open("input.txt","r").readlines()

# create a list to store numbers and positions
nums_array = list()

def part1():
    find_numbers(lines,nums_array)
    return find_parts(lines,nums_array)
    # return pn_checker(lines,nums_array)

# find every number's position in the matrix
def find_numbers(lines,nums_array):
    for line_num,this_line in enumerate(lines):
        for match in finditer(r'\d+', this_line):
            nums_array.append([line_num, match.group(), list(match.span()), False])   # legend: [line_num, matched number, span, is_pn:default False]
    for n in nums_array:
        n[2][1] = n[2][1]-1 # make the end of the span the actual end of the number

def find_parts(lines,nums_array):
    total_sum = 0

    for n in nums_array:

        thislinenum = n[0]
        
        # create a grid to search
        # we will traverse all the points in the grid. for example, for a three digit number somewhere inside array,
        # there will 5 possible points above, 5 on the same row(three digits are the number), and five points below.
        first_row = max(0,thislinenum - 1)
        last_row = min(len(lines)-1,thislinenum + 1)        # need to check these rows inclusive
        first_col = max(0,n[2][0]-1)
        last_col = min(len(lines[last_row]) - 1, n[2][1]+1) # need to check these columns inclusive

        # print(n[1],first_row,last_row,first_col,last_col)

        n[3] = traverse(first_row,last_row,first_col,last_col)

        if n[3] == True: total_sum += int(n[1])

    return total_sum

def traverse(first_row,last_row,first_col,last_col) -> bool:
    for row in lines[first_row:last_row+1]:
        for char in row[first_col:last_col+1]:
            if char not in '\n.0123456789': 
                return(True) # found a real symbol in the zone we're checking, literally just end the search and return
    return False

def part2():
    pass
    # if any two numbers have an adjacent star, we have to multiply the numbers.

    # amend part 1 to log where all the adjacent stars are
    # keep the star's location in a separate list including the index of the numbers in num
    # if two parts have a star in the same location, then we know it's a 
    # find the stars
    # count the numbers that surround a star

if __name__ == "__main__":
    part1()
    part2()
