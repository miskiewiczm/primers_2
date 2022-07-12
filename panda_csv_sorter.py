#!/usr/local/bin/python3

import pandas as pd
import sys

path = "./"
file_inn_name = str(sys.argv[1])
file_out_name = str(sys.argv[2])

print("From file ", path+file_inn_name, " to file ", path+file_out_name)
data = pd.read_csv(path+file_inn_name)
data_sort = data.sort_values(by=["any_th","3p_th","hairpin_th","gc_per","tm"])
data_sort.to_csv(path+file_out_name,  index=False)

print("Sorted.")