#function for Part 1 which just checks is current value in list is larger then previous.
def CountLargerList(input):
    larger = 0
    for index in range(1, len(input)):
        # if current depth is greater than previous depth add 1 to larger variable.
        cur_depth = input[index]
        prev_depth = input[index - 1]
        print_str = f"Index: {index}\tCur Depth: {cur_depth}\t Prev Depth: {prev_depth}\t"
        if cur_depth > prev_depth:
            larger += 1
            print_str += "IsDeeper: True\t"
        else:
            print_str += "IsDeeper: False\t"

        print_str += f"LargerCount: {larger}"
        print(print_str)

    return larger

def CountLargerSlice(input, slice_size = 3):
    larger = 0
    for index in range(1, len(input) -  slice_size + 1):
        cur_slice = input[index:index+slice_size]
        cur_slice_sum = sum(cur_slice)
        prev_slice = input[index-1:index+slice_size-1]
        prev_slice_sum = sum(prev_slice)
        print_str = f"CurSlice: {cur_slice}\tCurSliceSum: {cur_slice_sum}\tPrevSlice: {prev_slice}\tPrevSliceSum: {prev_slice_sum}\t"
        if cur_slice_sum > prev_slice_sum:
            larger += 1
            print_str += "IsDeeper: True"
        else:
            print_str += "IsDeeper: False"
        print_str += f"\tLargerCount: {larger}"
        print(print_str)

    return larger

if __name__ == "__main__":
    #change filename or create your own list of integers for input
    filename = "input.txt"
    input = open(filename, "r").read().splitlines()
    input = list(map(int, input))

    #Part 1
    num_larger = CountLargerList(input)
    print(f"The number of individual readings where depth increases: {num_larger}")

    #Part 2
    slice_size = 3
    num_larger = CountLargerSlice(input, slice_size)
    print(f"The number of slices with size {slice_size} where depth increases: {num_larger}")