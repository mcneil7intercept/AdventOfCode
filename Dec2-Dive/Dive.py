def part1(input):
    depth = 0
    horizantal = 0

    for value in input:
        print_str = f"Command: {value[0]}\tMagnitude: {value[1]}\t"
        mag = int(value[1])
        if value[0] == "forward":
            horizantal += mag
        elif value[0] == "up":
            depth -= mag
        else:
            depth += mag
        print_str += f"CurDepth: {depth}\tCurForward: {horizantal}"
        #print(print_str)
    
    return  depth, horizantal
    
def part2(input):
    depth = 0
    horizantal = 0
    aim = 0

    for value in input:
        print_str = f"Command: {value[0]}\tMagnitude: {value[1]}"
        mag = int(value[1])
        if value[0] == "forward":
            horizantal += mag
            depth += aim*mag
        elif value[0] == "up":
            aim -= mag
        else:
            aim += mag
        print_str += f"\tCurAim: {aim}\tCurDepth: {depth}\tCurForward: {horizantal}"
        #print(print_str)
    
    return  depth, horizantal

if __name__ == "__main__":
    values = [line.split() for line in open("input.txt").readlines()]
    testvalues = [line.split() for line in open("testinput.txt").readlines()]
    #print(values)

    # depth, distance = part1(values)
    # print(f"Final Depth: {depth}\tFinal Forward: {distance}\tMultiplied: {depth*distance}")

    depth, distance = part2(values)
    print(f"\tFinal Depth: {depth}\tFinal Forward: {distance}\tMultiplied: {depth*distance}")