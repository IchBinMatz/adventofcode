from rich import print

def parseInput(inp:str) -> list[tuple[list, list]]:
    def parseLine(s, lst: list) -> list:
        letter = next(s)
        while letter:
            match letter:
                case '[':
                    lst.append(parseLine(s,[]))
                case ',':
                    pass
                case ']':
                    return lst
                case number:
                    lst.append(int(number))
            letter = next(s)
                
    pairs = inp.strip().split('\n\n')
    returnList = []
    for pair in pairs:
        a,b = pair.splitlines()
        a_lst = parseLine(iter(a[1:]),[])
        b_lst = parseLine(iter(b[1:]),[])
        returnList.append((a_lst,b_lst))
    return returnList

def compare_pair(pair: tuple[list,list]):
    pass
    
    

if __name__ == "__main__":
    example = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
    """
    pairs_of_packets = parseInput(example)
    print(pairs_of_packets)
    for pair in pairs_of_packets:
        compare_pair(pair)
        
    