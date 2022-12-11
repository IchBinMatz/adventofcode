import math

from dataclasses import dataclass, field

from rich import print

from tqdm import tqdm


@dataclass
class Monkey:
    nr: int
    startingItems: list
    operation: callable = field(repr=False)
    test: int = field(repr=False)
    testtrue: int = field(repr=False)
    testfalse: int = field(repr=False)
    inspected: int = field(default=0)


def parse_input(inp: str):
    monkeystrings = inp.split("\n\n")
    monkeys = []
    for monkey in monkeystrings:
        nr: int = 0
        starting_items: list = []
        operation: str = ""
        test: int = ""
        testtrue: int = 0
        testfalse: int = 0
        for line in monkey.splitlines():
            if line.startswith("Monkey"):
                nr = int(line[7])
                continue
            match line.strip().split(": "):
                case "Starting items", items:
                    starting_items = [int(i) for i in items.split(", ")]
                case "Operation", op:
                    operation = parse_operation(op)
                case "Test", t:
                    test = int(t.split("by ")[1])
                case "If true", text:
                    testtrue = int(text.split("monkey ")[1])
                case "If false", text:
                    testfalse = int(text.split("monkey ")[1])
        monkeys.append(Monkey(nr, starting_items, operation, test, testtrue, testfalse))

    modulo = 1
    for m in monkeys:
        modulo *= m.test
    return monkeys, modulo


def parse_operation(op: str):
    match op.split():
        case "new", "=", "old", "*", "old":
            return lambda d: d * d
        case "new", "=", "old", "*", val:
            return lambda d: d * int(val)
        case "new", "=", "old", "+", val:
            return lambda d: d + int(val)
    return lambda x: x + 1


def step1(monkeys: list[Monkey], modulo: int) -> int:
    for round in tqdm(range(20)):
        play_a_round(monkeys, modulo, 1)
    sorted_monkeys = sorted(monkeys, key=lambda m: m.inspected, reverse=True)
    print(monkeys)
    return sorted_monkeys[0].inspected * sorted_monkeys[1].inspected


def play_a_round(monkeys: list[Monkey], modulo, part=1):
    for monkey in monkeys:
        for item in monkey.startingItems:
            worry_level = monkey.operation(item)
            if part == 1:
                worry_level = worry_level // 3
            worry_level = worry_level % modulo # This line was needed for part two
            monkey.inspected += 1
            next_monkey = 0
            if (worry_level % monkey.test) == 0:
                next_monkey = monkey.testtrue
            else:
                next_monkey = monkey.testfalse
            next(filter(lambda m: m.nr == next_monkey, monkeys)).startingItems.append(
                worry_level
            )
        monkey.startingItems = []


def step2(monkeys: list[Monkey], modulo: int) -> int:
    for round in tqdm(range(1,10001)):
        play_a_round(monkeys, modulo, 2)
    sorted_monkeys = sorted(monkeys, key=lambda m: m.inspected, reverse=True)
    print(monkeys)
    return sorted_monkeys[0].inspected * sorted_monkeys[1].inspected


if __name__ == "__main__":
    example = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip()
    monkeys, modulo = parse_input(example)
    print(monkeys)

    monkey_business = step1(monkeys, modulo)
    print(f"Monkey Business {monkey_business}")
    assert monkey_business == 10605

    monkeys, modulo = parse_input(example)
    monkey_business = step2(monkeys, modulo)
    print(f"Monkey Business {monkey_business}")
    assert monkey_business == 2713310158

    with open("input.txt", "r", encoding="utf8") as f:
        my_input = f.read().strip()
    monkeys, modulo = parse_input(my_input)
    monkey_business = step1(monkeys, modulo)
    print(f"Monkey Business {monkey_business}")
    
    monkeys, modulo = parse_input(my_input)
    monkey_business = step2(monkeys, modulo)
    print(f"Monkey Business {monkey_business}")

