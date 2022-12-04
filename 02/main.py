from typing import Literal
from rich import print

Hand = Literal["rock","paper","scissors"]


def main():
    with open("02/input.txt", 'r') as f:
        games = f.read().split("\n")
        games.pop() # remove empty line at the end
    

    print("What would your total score be if everything goes exactly according to your strategy guide?")
    print(sum([scoregame(game) for game in games]))


def scoregame(game : str) -> int:
    shapeMapping = {
        "A" : "rock",
        "B" : "paper",
        "C" : "scissors",
        "X" : "rock",
        "Y" : "paper",
        "Z" : "scissors",
    }

    pointMapping = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    opponent, me = [shapeMapping[x] for x in game.split(" ")]

    mypoints = pointMapping[me]
    gameresult = playgame(opponent, me)
    if gameresult == "right":
        mypoints += 6
    if gameresult == "draw":
        mypoints += 3
    # print(opponent, me, playgame(opponent, me), mypoints)
    return mypoints

def playgame(left : Literal["rock","paper","scissors"], right) -> Literal["left", "right", "draw"]:
    if (left == "rock" and right == "scissors"):
        return "left"
    if (left == "rock" and right == "paper"):
        return "right"
        
    if (left == "paper" and right == "scissors"):
        return "right"
    if (left == "paper" and right == "rock"):
        return "left"
        
    if (left == "scissors" and right == "rock"):
        return "right"
    if (left == "scissors" and right == "paper"):
        return "left"

    if (left ==  right):
        return "draw"
    raise NameError("komischer SpielFall")


if __name__ == "__main__":
    main()