#!/usr/local/bin/python3

import random


def random_string(length):
    return "".join(random.choice('ACTG') for _ in range(length))


file_name = "random_strings.txt"
file = open(file_name, "w")

n = 100

length = 540
target_start = 161
target_length = 160
target_end = target_start + target_length
end = "\n"
separator = " "

primer_1 = "GTCCTTTGATTCTCCTGTCC"
primer_2 = "GCTCCCTACCACCATTTACT"
# primer_1 = random_string(20)
# primer_2 = random_string(20)

for i in range(n):
    oligo = random_string(target_length)
    seq_start = random_string(target_start - 1 - 20)
    seq_end = random_string(length - 20 - target_start - target_length)
    sequence = seq_start + separator + primer_1 + separator + oligo + separator + primer_2 + separator + seq_end
    print(sequence)
