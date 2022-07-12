#!/usr/local/bin/python3

from numba import jit

import numpy as np
import sys
import time

path = "./"
name_in = str(sys.argv[1])
name_out = "primer_cross.csv"

file_in = open(path+name_in, "r")
count = 0
pointer = 0

@jit(parallel = True)
def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = []

        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
        return max(align)


#print("Scanning...")
for line in file_in:
    count = count + 1
#print(count, " lines scanned.")

cross = np.full((count, count),-1)

file_in.seek(0)
count_2 = 5
for i in range(count_2):
    start_t = time.time()
    file_in.seek(pointer)
    line = file_in.readline()
    primer_1 = line.split(",")[0]
    file_in.seek(pointer)
    for j in range(count-i):
        primer_2 = file_in.readline().split(",")[0]
        cross[i, j+i] = comparer(primer_1, primer_2)
    pointer = pointer + len(line)
    end_t = time.time()
    print(i,"\t",end_t - start_t, flush=True)

cross = cross + cross.T - np.diag(np.diag(cross))
np.savetxt(path+name_out, cross, delimiter=";", fmt="%i")