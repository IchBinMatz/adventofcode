from dataclasses import dataclass
from copy import deepcopy
from rich import print


@dataclass
class Stacks:
    stacks: list[list]

    def procedure9000(self, p: str):
        # parsing
        count, fromstack, tostack = [int(s) for s in p.split(" ") if s.isdigit()]
        for _ in range(count):
            self.stacks[tostack-1].append(self.stacks[fromstack-1].pop())
    def procedure9001(self, p: str):
        # parsing
        count, fromstack, tostack = [int(s) for s in p.split(" ") if s.isdigit()]
        moving = []
        for _ in range(count):
            moving.append(self.stacks[fromstack-1].pop())
        for _ in range(count):
            self.stacks[tostack-1].append(moving.pop())


def main(inp: str):
    stacks, procedures = inp.split("\n\n")
    print(stacks)
    s_original: Stacks = parseStacks(stacks)
    s = deepcopy(s_original)
    print(s)
    for p in procedures.splitlines():
        s.procedure9000(p)
    print(s)
    print("After the rearrangement procedure9000 completes, what crate ends up on top of each stack?")
    print("".join([stack.pop() for stack in s.stacks]))

    s = deepcopy(s_original)
    for p in procedures.splitlines():
        s.procedure9001(p)
    print(s)
    print("After the rearrangement procedure9001 completes, what crate ends up on top of each stack?")
    print("".join([stack.pop() for stack in s.stacks]))


def parseStacks(stacksstring: str) -> Stacks:
    lines = stacksstring.splitlines()
    numbers = [int(s, 10) for s in lines.pop().strip().split("   ")]
    anzahlStacks = numbers.pop()
    stacks = [[] for i in range(anzahlStacks)]
    for i in range(anzahlStacks):
        for line in reversed(lines):
            item = line[1 + i * 4]
            if item == " ":
                continue
            stacks[i].append(line[1 + i * 4])
    return Stacks(stacks)
    


if __name__ == "__main__":

    # example
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
    with open("input.txt", "r", encoding="utf8") as f:
        file = f.read()

    main(file)
