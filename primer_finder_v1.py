# Primer selector - primer source is a csv cross file.
# Version 0.0.2 with changes in seek_primer function
# needs more testing 

import numpy as np

name_in = "/Users/marek/primers/primers_cross_best.csv"
cross_matrix = np.genfromtxt(name_in, delimiter=',')

primers_chain = []

n_of_primers = 529
max_pos = 528
count = 0


def seek_primer(x, y, max_x, max_val):
    if y >= max_x: return -1
    i = y
    while cross_matrix[x][i] > max_val:
        i = i + 1
        if i > max_x: return -1
    return i


def check_primer(y, chain_pos, value):
    k = chain_pos
    while k > 0:
        if cross_matrix[y][primers_chain[k]] > value:
            return False
        k = k - 1
    return True


# initial primer selection as its number
row = 6
pos_x = 0
score = 5
primers_chain.append(row)

while count < n_of_primers:
    poi = seek_primer(row, pos_x, max_pos, score)
    if poi == -1:
        print("==========================")
        print("End of primers line, BREAK")
        break
    if check_primer(poi, count, score):
        print(count, poi, " - ACCEPTED.")
        primers_chain.append(poi)
        count = count + 1
    pos_x = poi + 1
print("==========================")
print(primers_chain)

name = "/Users/marek/primers/primers3_selected_best.txt"
file = open(name,"r")

for i in range(529):
    line = file.readline()
    if i in primers_chain[1:]:
#        print(">")
#        print(line[:-1])
         print(i)
file.close()
