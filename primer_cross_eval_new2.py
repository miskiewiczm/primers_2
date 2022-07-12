#!/usr/local/bin/python3

import sys

path = "./"
name_in = "primers_selected.csv"
name_out = "primer_cross.csv"

file_in = open(path + name_in, "r")


def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = "*" * (len(primer1 + primer2) - 2) + primer1
        p2_tab = "*" * (len(primer1) - 1) + primer2
        align = []

        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T"))
                + common.count(("T", "A"))
                + common.count(("C", "G"))
                + common.count(("G", "C"))
            )
        return max(align)


primer_1 = str(sys.argv[1])
score = 6
store = []
counter = 0
# store.append(primer_1)

for line in file_in:
    a = 0
    counter = counter + 1
    primer_2 = line.split(",")[0]
    x = comparer(primer_1, primer_2)
    if x <= score:
        for primer_3 in store:
            y = comparer(primer_2, primer_3)
            if y > score:
                a = 1
                break
        if a == 0:
            store.append(primer_2)
            print("pr" + str(counter) + "\t" + primer_2)
print(counter)
file_out = open("primers_small.txt", "w")
for line in store:
    file_out.write(line + "\n")
file_out.close()
