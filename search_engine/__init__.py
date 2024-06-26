"""
Data Lading Section ... 
"""
import os
from .utils import convert_str_to_list


seq_list: list
seq_list_names: list
seq_list_numeric: list
sequences_names_map: dict
sequences_terms_map: dict


def is_windows():
    return os.name == "nt"


def get_sequence_name(sequence: str):
    return sequence[0:sequence.find(',')].strip()


def get_sequence_terms_by_number(oeis_seq_number: int):
    if oeis_seq_number not in sequences_terms_map.keys():
        return ""
    sequence_from_db = seq_list[sequences_terms_map[oeis_seq_number]].strip().strip(",")
    sequence_after_removing_name = sequence_from_db[sequence_from_db.find(','):].strip().strip(",")
    return sequence_after_removing_name


def get_sequence_name_by_number(oeis_seq_number: int):
    if oeis_seq_number not in sequences_names_map.keys():
        return ""
    return seq_list_names[sequences_names_map[oeis_seq_number]].strip()


def load_data():
    global seq_list_names
    global seq_list, seq_list_numeric
    global sequences_names_map, sequences_terms_map

    # Load Strings
    last_modified = ""
    with open(os.path.join("data", "stripped"), encoding='utf-8') as f:
        seq_list = f.readlines()
    with open(os.path.join("data", "names"), encoding='utf-8') as f:
        seq_list_names = f.readlines()

    # Delete Metadata
    while not seq_list[0].startswith("A"):
        if "Last Modified:".lower() in seq_list[0].lower():
            last_modified = ":".join(seq_list[0].split(":")[1:]).strip()
        del seq_list[0]
        del seq_list_names[0]

    # Convert String into Numeric List
    seq_list_numeric = [[0]] * len(seq_list)
    for i in range(len(seq_list)):
        seq_list_numeric[i] = convert_str_to_list(seq_list[i])

    # Mapping Sequences Names with Indices (Loop for each one is necessary)
    sequences_names_map = {}
    sequences_terms_map = {}
    for i in range(len(seq_list_names)):
        seq_number = seq_list_names[i].split()[0]
        sequences_names_map[int(seq_number.strip("A"))] = i
    for i in range(len(seq_list)):
        seq_number = get_sequence_name(seq_list[i])
        sequences_terms_map[int(seq_number.strip("A"))] = i

    return last_modified


# Echo
print("[#]")
print("[+] Data Loading ... Please Wait .......")
last_modified = load_data()
last_added_seq_num = max(list(sequences_terms_map.keys()))
last_allocated_seq_num = max(list(sequences_names_map.keys()))
print(f"[+] Number of Available Sequences: {len(seq_list)}.")
print(f"[+] The last added sequence is {get_sequence_name_by_number(last_added_seq_num)}")
print(f"[+] The last allocated sequence is {get_sequence_name_by_number(last_allocated_seq_num)}")
print(f"[+] Last Modified on {last_modified}.")
print("[+] Data Loading is Done Successfully .......")
print("[#]")


from .fuzzy_matching import *
if not is_windows():
    from .formula_lookup import *
else:
    from .formula_lookup_win import *
from .normal_search import *
from .operation_design import *

from .advanced.engine1 import *
from .advanced.engine2 import *
from .advanced.engine3 import *
from .advanced.engine4 import *
from .advanced.engine5 import *
