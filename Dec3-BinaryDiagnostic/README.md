Link to instructions (sorry got tired of bad formatting):

    https://adventofcode.com/2021/day/3

First ideas, can either break each digit into it's own array and then count instances of non-zero numbers. (STILL DOABLE BUT PROBABLY SLOWER)

OR 

I think you can also use bit shifting and use just one array of values. (CHOSEN PATH)

My part 1 solution in written form: (I suck at these write ups)

1. Split input into a list of binary numbers
2. Assume each number has the same bit width called num_bits.
3. Loop from 1 to num_bits then AND every value in list of binary numbers with 2^(cur_bit_pos-1) 'clearing' out the other bits
4.  Count values in resulting list that are not zero and compare with number of elements in list to see if there are more 1s or 0s in that position.
5. If more ones set that bit in Gamma using an OR with 2^(cur_bit_pos-1)
6. Once completed calculate epsilon by computing the inverse of the resulting gamma value (epsilon = (1 << num_bits) - 1 - gamma)
7. Multiply those two values together for final result


