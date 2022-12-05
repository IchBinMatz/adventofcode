from rich import print
from dataclasses import dataclass, field


@dataclass
class Pair:
    input: str
    lstart : int = field(init=False)
    lend: int = field(init=False)
    rstart :int = field(init=False)
    rend: int = field(init=False)

    def __post_init__(self):
        left, right = self.input.split(",")
        self.lstart, self.lend = [int(n) for n in left.split("-")]
        self.rstart, self.rend = [int(n) for n in right.split("-")]

def hasFullyContaining(p: Pair) -> bool:
    if (p.lstart >= p.rstart) and (p.lend <= p.rend):
        return True
    if (p.rstart >= p.lstart) and (p.rend <= p.lend):
        return True
    return False

def hasOverlap(p:Pair) -> bool:
    if (p.lstart >= p.rstart) and (p.lstart <= p.rend):
        return True
    if (p.lend >= p.rstart) and (p.lend <= p.rend):
        return True
    if (p.rstart >= p.lstart) and (p.rstart <= p.lend):
        return True
    if (p.rend >= p.lstart) and (p.rend <= p.lend):
        return True
    return False

def main():
    with open("input.txt", "r") as f:
        pairs = [
            Pair(line)
            for line in f.read().splitlines()
        ]
    print(pairs[:3])
    uselessPairs = list(filter(hasFullyContaining, pairs))
    print("In how many assignment pairs does one range fully contain the other?")
    print(len(uselessPairs))

    print("In how many assignment pairs do the ranges overlap?")
    overlappingPairs = list(filter(hasOverlap, pairs))
    print(len(overlappingPairs))

if __name__ == "__main__":
    main()
