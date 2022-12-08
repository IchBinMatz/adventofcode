from dataclasses import dataclass


@dataclass
class Tree:
    height: int
    n: list
    e: list
    s: list
    w: list

    def isVisible(self) -> bool:
        return any([
            all([self.height > h for h in self.n]),
            all([self.height > h for h in self.e]),
            all([self.height > h for h in self.s]),
            all([self.height > h for h in self.w]),
        ])
    def scenic_score(self) -> int:
        if any([
            self.n == [],
            self.e == [],
            self.s == [],
            self.w == []
        ]):
            return 0
        north_score = 0
        for h in reversed(self.n):
            north_score += 1
            if h >= self.height:
                break;
        east_score = 0
        for h in self.e:
            east_score += 1
            if h >= self.height:
                break;
        south_score = 0
        for h in self.s:
            south_score += 1
            if h >= self.height:
                break;
        west_score = 0
        for h in reversed(self.w):
            west_score += 1
            if h >= self.height:
                break;
        return north_score*east_score*south_score*west_score
            
        


def main(inp: str):
    inp = inp.strip()
    visible_trees: int = 0
    lines = inp.splitlines()
    trees: list[Tree] = []
    for nr, line in enumerate(lines):
        for index, c in enumerate(line):
            height = int(c)
            north = [int(l[index]) for l in lines[:nr]]
            east = [int(h) for h in line[index + 1 :]]
            south = [int(l[index]) for l in lines[nr + 1 :]]
            west = [int(h) for h in line[:index]]

            trees.append(Tree(height, north, east, south, west))

    return trees

def step1(trees: list[Tree]):
    return len(list(filter(lambda t: t.isVisible(), trees)))

def step2(trees: list[Tree]):
    return max([t.scenic_score() for t in trees])

if __name__ == "__main__":
    example = """30373
25512
65332
33549
35390
    """
    trees = main(example)
    print(
        "Consider your map; how many trees are visible from outside the grid?"
    )
    print(step1(trees))
    assert step1(trees) == 21
    print(
        "Consider each tree on your map. What is the highest scenic score possible for any tree?"
    )
    scenic_score = step2(trees)
    print(scenic_score)
    assert scenic_score == 8

    with open("input.txt", "r", encoding="utf8") as f:
        my_input = f.read()
    trees = main(my_input)
    print(
        "Consider your map; how many trees are visible from outside the grid?"
    )
    print(step1(trees))
    print(
        "Consider each tree on your map. What is the highest scenic score possible for any tree?"
    )
    scenic_score = step2(trees)
    print(scenic_score)
