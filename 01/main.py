# https://adventofcode.com/2022/day/1
from rich import print
from dataclasses import dataclass, field
import requests

@dataclass
class Elve:
    id: int
    food: int
    calories: int = field(init=False)

    def __post_init__(self):
        self.calories = sum(self.food)

def main():
    # read in file
    data = []
    with open("01/input.txt", 'r') as f:
        data = f.read()
    
    elvesstrings = [s.split('\n') for s in data.split("\n\n")]
    elvesstrings[-1].pop() # last line was empty
    elves : list[Elve] = []
    for i, values in enumerate(elvesstrings,1):
        elve: Elve = Elve(i, [int(v) for v in values])
        elves.append(elve)

    sortedElves = sorted(elves, key=lambda elve: elve.calories)
    print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
    print(sortedElves)
    topElve = sortedElves[-1]
    print(f"Der Elf Nr {topElve.id} trägt {sum(topElve.food)} Calorien")

    print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
    print(sum([e.calories for e in sortedElves[-3:]]))


if __name__ == "__main__":
    main()