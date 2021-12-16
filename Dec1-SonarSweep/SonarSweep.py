#open our input
input = open("input.txt", "r").read().split("\n")

larger = 0
for index in range(1, len(input)):
    print(f"Index: {index}\tCurrent Depth: {input[index]}\t Previous Depth: {input[index-1]}")
    #if current depth is greater than previous depth add 1 to larger variable.
    if input[index] >= input[index - 1]:
        larger += 1

print(f"Number of reading where depth increases: {larger}")