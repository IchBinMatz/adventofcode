from typing import Literal
from rich import print

pointMapping = {"rock": 1, "paper": 2, "scissors": 3}


def main():
    with open("02/input.txt", "r") as f:
        games = f.read().split("\n")
        games.pop()  # remove empty line at the end

    print(
        "What would your total score be if everything goes exactly according to your strategy guide?"
    )
    print(sum([scoregame(game) for game in games]))

    print(
        "Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?"
    )
    print(sum([scoreGamePart2(game) for game in games]))


def scoreGamePart2(game) -> int:
    shapeMapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    opponent, me = [shapeMapping[x] for x in game.split(" ")]
    if me == "draw":
        me = opponent
    if me == "win":
        if opponent == "rock":
            me = "paper"
        if opponent == "paper":
            me = "scissors"
        if opponent == "scissors":
            me = "rock"
    if me == "lose":
        if opponent == "rock":
            me = "scissors"
        if opponent == "paper":
            me = "rock"
        if opponent == "scissors":
            me = "paper"
    
    gameresult = playgame(opponent, me)
    mypoints = pointMapping[me]
    if gameresult == "right":
        mypoints += 6
    if gameresult == "draw":
        mypoints += 3
    
    print(f"{opponent} vs. {me} - result: {gameresult}")
    return mypoints


def scoregame(game: str) -> int:
    shapeMapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
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


def playgame(
    left: Literal["rock", "paper", "scissors"],
    right: Literal["rock", "paper", "scissors"],
) -> Literal["left", "right", "draw"]:
    if left == "rock" and right == "scissors":
        return "left"
    if left == "rock" and right == "paper":
        return "right"

    if left == "paper" and right == "scissors":
        return "right"
    if left == "paper" and right == "rock":
        return "left"

    if left == "scissors" and right == "rock":
        return "right"
    if left == "scissors" and right == "paper":
        return "left"

    if left == right:
        return "draw"
    
    raise NameError("komischer SpielFall")


if __name__ == "__main__":
    main()
