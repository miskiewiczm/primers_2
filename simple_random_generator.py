#!/usr/local/bin/python3
# run:
# ./simple_random_generator output_file num_of_primers primer_length
import primer3
import random
import sys


def check_runs(prim):
    return not ('AAAAA' in prim or 'CCCCC' in prim or 'TTTTT' in prim or 'GGGGG' in prim)


def check_temp(prim, tmin, tmax):
    tm = primer3.calcTm(prim, mv_conc=50, dv_conc=4, dntp_conc=0.5, dna_conc=50)
    return tmin < tm < tmax


def check_gc(prim, gcmin, gcmax):
    c = (prim.count('C') + prim.count('G')) / float(l)
    return gcmin < c < gcmax


def check_repeats(prim):
    repeats = ["ATATATAT", "ACACACAC", "AGAGAGAG", "CACACACA", "CGCGCGCG", "CTCTCTCT", "TATATATA", "TCTCTCTC",
               "TGTGTGTG", "GAGAGAGA", "GCGCGCGC", "GTGTGTGT"]
    for repeat in repeats:
        if bool(prim.find(repeat) + 1):
            # print(prime, " --- ", repeat)
            return False
    return True


k = int(sys.argv[2])
l = int(sys.argv[3])
n = 0
tm_min = 58.0
tm_max = 62.0
gc_min = 0.48
gc_max = 0.52
counter = 0
divider = k/10


file_name = str(sys.argv[1])
print(file_name)
path = "./"


file = open(path + file_name, "w")
while counter < k:
    primer = "".join(random.choice('ACTG') for _ in range(l))
    if check_runs(primer):
        if check_gc(primer, gc_min, gc_max):
            if check_temp(primer, tm_min, tm_max):
                if check_repeats(primer):
                    counter += 1
                    if counter % divider == 0:
                        print(counter, end=" ", flush=True)
                    file.write(primer + "\n")

    n += 1
file.close()
print("\n", n, " - ", k / n)
