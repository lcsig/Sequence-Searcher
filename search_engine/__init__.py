"""
Data Lading Section ... 
"""
import os
from .seq import convert_str_to_list


# Echo & Definitions
print("[+] Data Loading ... Please Wait ...")
seq_list: list
seq_list_numeric: list

# Loading Strings
with open(os.path.join("data", "stripped")) as f:
    seq_list = f.readlines()
del seq_list[0:4]

# Loading Integers
seq_list_numeric = [[0]] * len(seq_list)
for i in range(len(seq_list)):
    seq_list_numeric[i] = convert_str_to_list(seq_list[i])
print("[+] Data Loading is Done Successfully ...")



from .fuzzy_matching import *
from .formula_lookup import *
from .normal_search import *

from .advanced.engine1 import *
from .advanced.engine2 import *
from .advanced.engine3 import *
from .advanced.engine4 import *
from .advanced.engine5 import *
