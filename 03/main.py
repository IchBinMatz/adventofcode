from rich import print
from dataclasses import dataclass, field


@dataclass
class Rucksack:
    content: str
    left: str = field(init=False)
    right: str = field(init=False)
    commonItem: str = field(init=False)

    def __post_init__(self):
        self.left = self.content[: len(self.content) // 2]
        self.right = self.content[len(self.content) // 2 :]
        self.commonItem = list(set(self.left).intersection(self.right)).pop()

@dataclass
class Group:
    rucksacks: list[Rucksack]
    badge: str = field(init=False)

    def __post_init__(self):
        sets = [set(r.content) for r in self.rucksacks]
        self.badge = sets[0].intersection(sets[1]).intersection(sets[2]).pop()

def getPriority(letter: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(letter) + 1


def main():

    with open("03/input.txt") as f:
        rucksacks = [Rucksack(l) for l in f.read().splitlines()]
    print(
        "Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?"
    )
    print(sum([getPriority(rucksack.commonItem) for rucksack in rucksacks]))

    # grouping
    groups : list[Group] = [Group(rucksacks[i:i+3]) for i in range(0,len(rucksacks),3)]
    print(
        "Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?"
    )

    print(sum([getPriority(g.badge) for g in groups]))


if __name__ == "__main__":
    main()
