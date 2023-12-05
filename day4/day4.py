import os
import re
from collections import Counter

os.chdir("/Users/mattgardner/Documents/advent-of-code/day4")

# read in the input
lines = open("input.txt","r").readlines()

cards = list() # usage: card number, list of winning numbers, list of your numbers, score of the matches

total_sum = 0

def ingest(lines):
    for line in lines:
        card_num = re.search(r'\d+',line).group()
        splitup = re.split(':  |: | \| |\|  ',line.strip())
        cards.append([card_num,re.split('  | ',splitup[1]),re.split('  | ',splitup[2]),0]) # every card inits to zero matches until matches are computed

def compute_score(cards):
    # do the matches
    for card in cards:
        winners = Counter(card[1])
        your_nums = Counter(card[2])
        matches_count = sum((winners & your_nums).values())
        # compute points
        # one point for the first win, then 
        if matches_count > 0:
            if matches_count == 1:
                card[3] = 1 # exactly one match
            else:
                card[3] = 2**(matches_count - 1) # doubling with more matches
        else:
            card[3] = 0
        # print(card[0],card[3])
        

def part1(lines,cards):
    global total_sum
    ingest(lines)
    compute_score(cards) # this already saves scores to the cards list
    for card in cards:
        total_sum += card[3]

    return(total_sum)

if __name__ == "__main__":
    print("part1",part1(lines,cards))

