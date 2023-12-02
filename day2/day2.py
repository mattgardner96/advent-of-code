import os
import re

os.chdir("/Users/mattgardner/Documents/advent-of-code/day2")

# read in the input
lines = open("input.txt","r").readlines()


def part1(lines):
    print('part1')

    max_vals = {"red":12,"green":13,"blue":14}
    
    total_sum_line_nums = 0
    
    for line_num,line in enumerate(lines):              # each game
        hands = re.split(' |, |;|: ',line.strip())
        hands.pop(0)                    # strip off "Game", we're iterating anyway and it starts in column 0
        hands.pop(0)                    # strip off line number
        hands.remove('')                # clean data

        good_game = True
        
        # create dictionary of red, green, and blue
        colors_vals = {"red":0,"green":0,"blue":0}

        for color in colors_vals: # for each color
            if color in hands:
                for i,match in enumerate(hands):
                    if color == match:
                        colors_vals[color] += int(hands[i-1]) # this is the count at the end of the line
        
            if (colors_vals[color] > max_vals[color]):
                good_game = False
                break                   # if any are over, I don't care about the others
        print("line:",line_num+1," vals: ",colors_vals)
        
        if good_game:
            print(line_num+1)
            total_sum_line_nums += (line_num+1)

    return(total_sum_line_nums)

def part2(lines):
    pass


if __name__ == "__main__":
    print(part1(lines))

