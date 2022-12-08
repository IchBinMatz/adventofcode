import os
import time
from dataclasses import dataclass, field


@dataclass
class MyDir:
    name: str
    children: list = field(default_factory=lambda: [])

    def print(self, intendation=1):
        print(" " * intendation, end="")
        print(f"-{self.name}/")
        for c in self.children:
            c.print(intendation + 1)

    def get_size(self) -> int:
        size = 0
        for item in self.children:
            if isinstance(item, MyFile):
                size += item.size
            if isinstance(item, self.__class__):
                size += item.get_size()
        return size


@dataclass
class MyFile:
    name: str
    size: int

    def print(self, intendation=1):
        print(" " * intendation, end="")
        print("-", end="")
        print(self.name, self.size)


def main(inp: str) -> list[MyDir]:
    root = parse_lines(inp)
    root.print()
    return get_dirs(root)

def get_dirs(directory : MyDir) -> list[MyDir]:
    retlist = [directory]
    for c in directory.children:
        if isinstance(c, MyDir):
            retlist.extend(get_dirs(c))
    return retlist

def parse_lines(text: str) -> MyDir:
    lines = text.splitlines()
    root_dir: MyDir = MyDir("")
    current_dir: MyDir = root_dir
    dir_history: list[MyDir] = [root_dir]
    for line in lines:
        if line.startswith("$"):
            # os.system('clear')
            # print(dir_history[-1].name, current_dir.name)
            # print(root_dir.print())
            # time.sleep(0.1)
            _, cmd, *arg = line.split(" ")
            if cmd == "cd":
                if arg[0] == "..":
                    current_dir = dir_history.pop()
                    continue
                if arg[0] == "/":
                    dir_history = [root_dir]
                    current_dir = root_dir
                    continue
                dir_history.append(current_dir)
                if arg[0] in [d.name for d in current_dir.children]:
                    current_dir = next(
                        filter(lambda d: d.name == arg[0], current_dir.children)
                    )
                else:
                    current_dir = MyDir(name=arg[0])
                continue
            if cmd == "ls":
                continue
        size, name = line.split(" ")
        if name in [d.name for d in current_dir.children]:
            continue
        if size == "dir":
            current_dir.children.append(MyDir(name=name))
            continue
        current_dir.children.append(MyFile(name, int(size)))
    return root_dir

def step1(dirs: list[MyDir]) -> int:
    return sum(filter(lambda s: s<100000, [d.get_size() for d in dirs]))

def step2(dirs: list[MyDir]) -> int:
    disc_space = 70_000_000
    update_space = 30_000_000
    free_space = disc_space - dirs[0].get_size()
    needed_space = update_space - free_space
    def smallesUsefullDir(d: MyDir) -> bool:
        if d.get_size() > needed_space:
            return True
        return False

    return min([d.get_size() for d in filter(smallesUsefullDir, dirs)])

if __name__ == "__main__":
    example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    dirs = main(example)
    # Example test
    assert step1(dirs) == 95437

    with open("input.txt", "r", encoding="utf8") as f:
        myinput = f.read()
    
    dirs = main(myinput)
    print(
        "Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?"
    )
    print(step1(dirs))

    print(
        "Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?"
    )
    print(step2(dirs))