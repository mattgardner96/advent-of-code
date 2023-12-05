import os
import re
from collections import Counter

os.chdir("/Users/mattgardner/Documents/advent-of-code/day4")

# read in the input
lines = open("test.txt","r").readlines()

cards = list() # usage: card number, list of winning numbers, list of your numbers, score of the matches

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
        matches_count = sum((winners & your_nums).values())
        

def part1(lines,cards):
    ingest(lines)
    compute_wins(cards) # this already saves wins to the cards list, we can calculate wins 

if __name__ == "__main__":
    part1(lines,cards)

