command_cycles = {
    "noop": 1,
    "addx": 2
}

def step1(inp : str):
    lines =  iter(inp.splitlines())
    cycle = 1
    x = 1
    current_cmd = ""
    current_completion = 0
    argument = 0
    signal_strength = 0
    print("start")
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    crt_image : str = """
........................................
........................................
........................................
........................................
........................................
........................................
""".strip()
    while cycle <= 220:
        # start
        if(current_completion == 0):
            current_cmd, *arg = next(lines).split(" ")
            current_completion = command_cycles[current_cmd]
            if (arg):
                argument = arg[0]
        
        # during
        print(f"{cycle}: {current_cmd} X:{x}")
        if cycle in relevant_cycles:
            signal_strength += cycle* x

        # end
        cycle += 1
        current_completion -= 1
        if(current_completion == 0 and current_cmd == 'addx'):
            x += int(argument)
    print("finished")
    return signal_strength

def step2(inp : str):
    def set_sprite_position(x: int):
        string = []
        for i in range(40):
            if i == x+1:
                string.append('#')
            elif i == x-1:
                string.append('#')
            elif i == x:
                string.append('#')
            else:
                string.append('.')
        return ''.join(string)
    lines =  iter(inp.splitlines())
    cycle = 1
    x = 1
    current_cmd = ""
    current_completion = 0
    argument = 0
    print("start")
    sprite_position = set_sprite_position(x)
    crt_image = []
    crt_current_row = []
    print(f"Sprite position: {sprite_position}")
    while cycle:
        # start
        if(current_completion == 0):
            try:
                current_cmd, *arg = next(lines).split(" ")
            except StopIteration:
                break
            current_completion = command_cycles[current_cmd]
            if (arg):
                argument = arg[0]
                print(f"Start Cycle {cycle:3}: begin executing {current_cmd} {argument}")
        
        # during
        crt_position = (cycle-1) % 40
        print(f"During Cycle{cycle:3}: CRT draws pixel in position {crt_position}")
        crt_current_row.append(sprite_position[crt_position])
        print(f"Current CRT row: {''.join(crt_current_row)}")
        # end
        cycle += 1
        if (cycle-1) % 40 == 0:
            crt_image.append(''.join(crt_current_row))
            crt_current_row = []
        current_completion -= 1
        if(current_completion == 0 and current_cmd == 'addx'):
            x += int(argument)
            print(f"End of Cycle{cycle:3}: finish executing addx {argument}")
            sprite_position = set_sprite_position(x)
            print(f"Sprite position: {sprite_position}")
        print()
    print("finished")
    return '\n'.join(crt_image)


if __name__ == "__main__":
    with open("example.txt", "r", encoding="utf8") as f:
        example = f.read().strip()
    signal_strength = step1(example)
    assert signal_strength == 13140
    print(f"summe der signalstärke ist: {signal_strength}")

    
    with open("input.txt", "r", encoding="utf8") as f:
        my_input = f.read().strip()
    signal_strength = step1(my_input)
    print(f"summe der signalstärke ist: {signal_strength}")

    crt_image = step2(example)
    assert crt_image == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    print(crt_image)

    crt_image = step2(my_input)
    print(crt_image)
