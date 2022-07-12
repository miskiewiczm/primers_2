#!/usr/local/bin/python3

import random
import sys


def random_string(length):
    return "".join(random.choice('ACTG') for _ in range(length))


length = 540
target_start = 161
target_length = 160
target_end = target_start + target_length
task = "generic"
seqid = "example"
end = "\n"

primer_1 = "GTCCTTTGATTCTCCTGTCC"
primer_2 = "GCTCCCTACCACCATTTACT"
# primer_1 = random_string(20)
# primer_2 = random_string(20)
oligo = random_string(target_length)
# oligo_1 = random_string(int(target_length / 2) - 5)
# oligo_2 = random_string(int(target_length / 2) - 5)
seq_start = random_string(target_start - 1 - 20)
seq_end = random_string(length - 20 - target_start - target_length)
sequence = seq_start + primer_1 + oligo + primer_2 + seq_end

# print(len(seq_start), len(primer_1), len(oligo), len(primer_2), len(seq_end))

file_in_name = "primer3_settings.txt"
file_out_name = "primer3_input.txt"

sequence_id = "SEQUENCE_ID=" + seqid + end
sequence_template = "SEQUENCE_TEMPLATE=" + sequence + end
sequence_target = "SEQUENCE_TARGET=" + str(target_start) + "," + str(target_length) + end
primer_task = "PRIMER_TASK=" + task + end
pick_l_primer = "PRIMER_PICK_LEFT_PRIMER=1" + end
pick_r_primer = "PRIMER_PICK_RIGHT_PRIMER=1" + end

file_in = open(file_in_name, "r")
file_out = open(file_out_name, "w")

for line in file_in:
    file_out.write(line)

file_out.write(sequence_template)
file_out.write(sequence_target)
file_out.write("=")
file_out.close()
file_in.close()
