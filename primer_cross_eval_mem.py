#!/usr/local/bin/python3

#from numba import jit

import numpy as np
import sys
import time

path = "./"
name_in = str(sys.argv[1])
name_out = "primer_cross.csv"

file_in = open(path+name_in, "r")
count = 0
pointer = 0

#@jit
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

base = []

print("Scanning...")
for line in file_in:
    base.append(line.split(",")[0])
count = len(base)
print(count)

cross = np.full((count, count),-1)

for i in range(5):
#    start_t = time.time()
    primer_1 = base[i]
    for j in range(count-i):
        primer_2 = base[i+j]
        cross[i, j+i] = comparer(primer_1, primer_2)
    print(i)
#    end_t = time.time()
#    print(i,"\t",end_t - start_t, "\t", primer_1)

# cross = cross + cross.T - np.diag(np.diag(cross))
# np.savetxt(path+name_out, cross, delimiter=";", fmt="%i")