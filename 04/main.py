from rich import print
from dataclasses import dataclass, field


@dataclass
class Pair:
    left: str
    right: str
    lsections: list[int] = field(init=False)
    rsections: list[int] = field(init=False)
    hasFullyContaining: bool = field(init=False)

    def __post_init__(self):
        start, end = [int(s) for s in self.left.split("-")]
        self.lsections = list(range(start, end + 1))
        start, end = [int(s) for s in self.right.split("-")]
        self.rsections = list(range(start, end + 1))
        self.hasFullyContaining = set(self.rsections).issubset(self.lsections) or set(
            self.rsections
        ).issubset(self.lsections)


def main():
    with open("04/input.txt", "r") as f:
        pairs = [
            Pair(line.split(",")[0], line.split(",")[1])
            for line in f.read().splitlines()
        ]

    hasFullyContaining: list[Pair] = []
    for pair in pairs:
        if set(pair.rsections).issubset(pair.lsections):
            hasFullyContaining.append(pair)
            continue  # so wird im fall, wenn beide gleich sind das object nicht zweimal hinzugefügt
        if set(pair.rsections).issubset(pair.lsections):
            hasFullyContaining.append(pair)

    hasFullyContaining = list(filter(lambda pair: pair.hasFullyContaining, pairs))
    print(hasFullyContaining[:3])
    print("In how many assignment pairs does one range fully contain the other?")
    print(len(hasFullyContaining))


if __name__ == "__main__":
    main()
