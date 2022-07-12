#!/usr/local/bin/python3

import os

pos_x = 0
pos_y = 0

data_file_name = "data_2.csv"
primer3_input_gen = "./pr3_tests.py"
primer3_run = (
    "./primer3_core ~/Mój\ dysk/Paradise_project/program/primer3_input.txt > temp.txt"
)

data_file = open(data_file_name, "w")
data_file.write("left_pr, right_pr\n")

number = 1000

for n in range(number):

    if n % 100 == 0:
        print(n, flush=True)

    os.chdir("/Users/marek/Mój dysk/Paradise_project/program")
    os.system(primer3_input_gen)
    os.chdir("/Users/marek/Downloads/primer3-2.4.0/src")
    os.system(primer3_run)

    file = open("temp.txt", "r")
    for line in file:
        line_list = line.split("=")
        if line_list[0] == "PRIMER_LEFT_0":
            pos_x = int(line_list[1].split(",")[0])
        if line_list[0] == "PRIMER_RIGHT_0":
            pos_y = int(line_list[1].split(",")[0])
    file.close()

    data_file.write(str(pos_x) + ", " + str(pos_y) + "\n")

data_file.close()
