#!/usr/local/bin/python3

import sys

file_inn_name = str(sys.argv[1])
file_out_name = str(sys.argv[2])
path = "./"

file_in = open(path+file_inn_name, "r")
file_out = open(path+file_out_name, "w")
header = "sequence,tm,gc_per,any_th,3p_th,hairpin_th\n"
file_out.write(header)
for line in file_in:
    if line[0:5] == "OLIGO":
        line = file_in.readline().split()
        tm = line[3]
        gc = line[4]
        any_th = line[5]
        p3_th = line[6]
        hairpin = line[7]
        sequence = line[8]
        file_out.write(sequence + "," + tm + "," + gc + "," + any_th + "," + p3_th + "," + hairpin + "\n")
file_in.close()
file_out.close()
