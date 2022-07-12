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

dna_dict = {"A":1, "C":2, "T":3, "G":4}

@jit
def comparer(primer1, primer2):

    primer2 = primer2[::-1]
    p1_tab = np.hstack((np.zeros(len(primer1 + primer2) - 2), primer1))
    p2_tab = np.hstack((np.zeros(len(primer1) - 1), primer2))
    align = []

    for i in range(len(primer1 + primer2) - 1):
        common = list(zip(p1_tab[i:], p2_tab))
        align.append(
            common.count((1, 3)) + common.count((3, 1)) +
            common.count((2, 4)) + common.count((4, 2))
        )
    return max(align)

base = []

print("Scanning...")
for line in file_in:
    base.append(line.split(",")[0])
count = len(base)
print(count)

basenp = np.zeros((count,20))

row, column = 0,0
for primer in base:
    for letter in primer:
        basenp[row, column] =  dna_dict[letter]
        column += 1
    column = 0
    row += 1

cross = np.full((count, count),-1)

time_avr = 0

for i in range(count):
    start_t = time.time()
    primer_1 = basenp[i]
    for j in range(count-i):
        primer_2 = basenp[i+j]
        cross[i, j+i] = comparer(primer_1, primer_2)
    end_t = time.time()
    time_avr += (end_t - start_t)
    if i % 100 == 0:
#        print(i,"\t",end_t - start_t, "\t", primer_1)
        print(i,"\t",time_avr/100 )
        time_avr = 0
# cross = cross + cross.T - np.diag(np.diag(cross))
# np.savetxt(path+name_out, cross, delimiter=";", fmt="%i")
