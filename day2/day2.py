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
                        this_color_num = int(hands[i-1])
                        if (this_color_num > max_vals[color]):
                            good_game = False
                            break           # if any are over, I don't care about the others
        
        if good_game:
            print(line_num+1)
            total_sum_line_nums += (line_num+1)

    return(total_sum_line_nums)

def part2(lines):
    print('part1')

    power_sum = 0

    for line_num,line in enumerate(lines):              # each game
        hands = re.split(' |, |;|: ',line.strip())
        hands.pop(0)                    # strip off "Game", we're iterating and it starts at row 0
        hands.pop(0)                    # strip off line number
        hands.remove('')                # clean data
        
        # create dictionary of red, green, and blue
        colors_vals = {"red":0,"green":0,"blue":0}

        power = 1

        for color in colors_vals: # for each color
            if color in hands:
                for i,match in enumerate(hands): 
                    if color == match:
                        colors_vals[color] =  max(colors_vals[color],int(hands[i-1])) # this *should* contain the max of each color
            power *= colors_vals[color]
        print("colors_vals:",colors_vals,"power",power)

        power_sum += power

    return(power_sum)




if __name__ == "__main__":
    # print(part1(lines))

    print(part2(lines))

