def Part1(binary_string_list):
    input_length = len(binary_string_list)
    num_bits = len(binary_string_list[0])
    shift = 2**(num_bits-1)
    format_str = '#0' + str(num_bits+2) + 'b'
    gamma = 0
    numbers = [int(value, 2) for value in binary_string_list]
    print(f"Input Count: {input_length}", f"Bit Width: {num_bits}")


    for i in range(num_bits):
        cur_shift = shift>>i
        not_zero = sum(map(lambda x : x > 0, [number&cur_shift for number in numbers]))
        if not_zero > (input_length - not_zero):
            gamma |= cur_shift
        print(f"NumBitsSet: {not_zero}", f"CurGamma(dec): {gamma}", f"CurGamma(bin): {format(gamma, format_str)}")

    epsilon = (1 << num_bits) - 1 - gamma
    return gamma, epsilon

def Part2(binary_string_list):
    return

if __name__ == "__main__":
    binary_string_list = open("input.txt").read().splitlines()
    gamma, epsilon = Part1(binary_string_list)
    print(f"Final Gamma: {gamma}", f"Final Epsilon {epsilon}", f"Multiplied {gamma*epsilon}")