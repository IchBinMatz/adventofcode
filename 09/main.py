import os
from dataclasses import dataclass

@dataclass
class Position():
    x:int
    y:int

    def moveTo(self, Another: Position):
        diffy = Another.y - self.y
        diffx = Another.x - self.x
        if (diffx == 0 and diffy > 1):
            self.y += 1
        if (diffx == 0 and diffy < -1):
            self.y -= 1
        if (diffx > 1 and diffy == 0):
            self.x += 1
        if (diffx < 1 and diffy == 0):
            self.x -= 1
            


@dataclass
class Grid():
    H: Position
    T: Position
    s: Position = Position(0,0)

def main(inp: str):
    visitedT = []
    T = Position(0,0)
    H = Position(0,0)
    os.system("clear")
    for line in inp.splitlines():
        print(line)
        direction, steps = line.split()
        moveAndFollow(direction, steps, H, T)
        print(H, T)

def moveAndFollow(direction,steps,head,tail):
    visited : list[Position] = [tail]
    for step in steps:
        match direction:
            case 'R' : head.x += 1
            case 'L' : head.x -= 1
            case 'U' : head.y += 1
            case 'D' : head.y -= 1
        
    return (head, tail, visited)
    
                
                

if __name__ == "__main__":
    example = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
    """.strip()
    main(example)