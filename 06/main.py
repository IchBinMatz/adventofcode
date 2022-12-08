def step1(inp: str):
    for i in range(len(inp)-4):
        numbers = set(inp[i:i+4])
        if len(numbers) == 4:
            return i+4

def step2(inp: str):
    for i in range(len(inp)-14):
        numbers = set(inp[i:i+14])
        if len(numbers) == 14:
            return i+14

if __name__ == "__main__":
    example="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    
    with open("input.txt", 'r', encoding='utf8') as f:
        inp = f.read()


    print(
        "EXAMPLE: How many characters need to be processed before the first start-of-packet marker is detected?"
    )
    print(step1(example))


    print(
        "puzzle1: How many characters need to be processed before the first start-of-packet marker is detected?"
    )
    print(step1(inp))

    print(
        "EXAMPLE2: How many characters need to be processed before the first start-of-packet marker is detected?"
    )
    print(step2(example))

    print(
        "puzzle2: How many characters need to be processed before the first start-of-packet marker is detected?"
    )
    print(step2(inp))
    