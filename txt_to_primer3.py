#!/usr/local/bin/python3

import sys

path = "./"
file_in_name = str(sys.argv[1])
file_out_name = str(sys.argv[2])

file_in = open(path+file_in_name, "r")
file_out = open(path+file_out_name, "w")

print(file_in_name, " --> ", file_out_name,"\n", flush=True)

end = "\n"
seq_id = "sample_06.08.2021"
task = "check_primers"
psm = 50.0
psd = 4.0
pdc = 0.5
pnc = 50.0

file_out.write("SEQUENCE_ID=" + seq_id + end)
file_out.write("PRIMER_TASK=" + task + end)
file_out.write("PRIMER_SALT_MONOVALENT=" + str(psm) + end)
file_out.write("PRIMER_SALT_DIVALENT=" + str(psd) + end)
file_out.write("PRIMER_DNTP_CONC=" + str(pdc) + end)
file_out.write("PRIMER_DNA_CONC=" + str(pnc) + end)
for primer in file_in:
    file_out.write("SEQUENCE_PRIMER=" + primer)
    file_out.write("=\n")

