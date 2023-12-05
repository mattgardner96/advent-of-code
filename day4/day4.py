import os
import re
from collections import Counter

os.chdir("/Users/mattgardner/Documents/advent-of-code/day4")

# read in the input
lines = open("input.txt","r").readlines()

cards = list() # usage: card number, list of winning numbers, list of your numbers, number of matches per card

total_sum = 0

def ingest(lines):
    for line in lines:
        card_num = re.search(r'\d+',line).group()
        splitup = re.split(':  |: | \| |\|  ',line.strip())
        cards.append([card_num,re.split('  | ',splitup[1]),re.split('  | ',splitup[2]),0]) # every card inits to zero matches until matches are computed

def compute_wins(cards):
    # do the matches
    for card in cards:
        winners = Counter(card[1])
        your_nums = Counter(card[2])
        card[3] = sum((winners & your_nums).values())
        
def part1(lines,cards):
    global total_sum
    ingest(lines)
    compute_wins(cards) # this already saves scores to the cards list

    this_score = 0
    # compute points
    # one point for the first win, then 

    for card in cards:
        if card[3] > 0:
            if card[3] == 1:
                this_score = 1 # exactly one match
            else:
                this_score = 2**(card[3] - 1) # doubling with more matches
        else:
            this_score = 0
        
        total_sum += this_score

    return(total_sum)

def part2(cards):
    big = list()
    index = 0
    length = 1 # should be 1 to start with
    big = cards # all the originals are there
    
    while index < length: # index is the index in the list we're actively building

        # just add the copies
        current_card = big[index]

        for i in range(0,current_card[3]):
            big.append(cards[int(current_card[0])+i])

        length = len(big)
        index += 1

    # for c in big:
    #     print(c)

    return(len(big))

if __name__ == "__main__":
    part1(lines,cards)
    print("part2",part2(cards))

