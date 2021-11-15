"""
This code contains a set of functions that will be used in the OEIS Search Engine
"""
import re
import modules.search_engine as eng


def is_seq_contains_fixed_numbers(sequence: str):
    """
    sequence: A string that contains a comma seperated numbers
    return: True if one of the terms is an integer, False if all terms are patterns
    """
    seq_terms = sequence.split(",")
    for term in seq_terms:
        if str(term).strip().lstrip("+-").isdigit():
            return True
    return False


def convert_str_to_list(sequence: str, is_ordered_sequence: bool = True, is_first_term_seq_name: bool = True):
    """
    sequence: A string that contains a comma seperated numbers
    is_first_term_seq_name: True to drop the first term (i.e. A01255,1,3,5, ...)
    return: A list of integers in a list (String ---> List)
    """
    terms_split: list
    if is_ordered_sequence:
        terms_split = sequence.split(",")
    else:
        terms_split = sequence.split(" ")

    if is_first_term_seq_name:
        del terms_split[0]  # Delete the name of the sequence
        del terms_split[-1]  # Delete the new line

    int_list: list = [0] * (len(terms_split))
    for idx in range(0, len(terms_split)):
        int_list[idx] = int(terms_split[idx])

    return int_list


def is_pattern_exist(seq: str):
    """
    Check the existence of patterns in the sequence
    seq: A string that contains a comma seperated numbers
    returns: True if there is a string pattern in the sequence.
    """
    pattern_exist = False
    pattern_exist = pattern_exist or ("?" in seq)
    pattern_exist = pattern_exist or ("--" in seq)
    return pattern_exist


def print_seq(numeric_seq):
    print("    Current Seq ---> ")
    for n in range(len(numeric_seq)):
        print(str(numeric_seq[n]) + ", ", end='')
    print("\n[#]")


def is_all_terms_are_fixed_numbers(sequence: str):
    """
    This method checks whither the sequence consists of numbers (i.e. no patterns)
    sequence: A string that contains a comma seperated numbers
    returns: True if the sequence contains numbers only, False otherwise.
    """
    seq_terms = sequence.split(",")
    for term in seq_terms:
        if not str(term).strip().lstrip("+-").isdigit():
            return False
    return True


def is_prime(num: int):
    """
    A function to check if a number is a prime number
    num: The number to be checked
    returns: True if num is a prime, False otherwise.
    """
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * num) is None


def generate_primes(start_prime: int, end_prime: int):
    """
    A function to generate a list of primes
    start_prime: The start prime/point
    start_prime: The end prime/point
    returns: A list contains primes where list[0] == the prime after or equal to start_prime
        and list[-1] == the prime that is before or equal to end_prime
    """
    primes_list = []

    for idx in range(start_prime, end_prime + 1):
        if is_prime(idx):
            primes_list.append(idx)

    return primes_list


def list_a_in_b(a: list, b: list):
    """
    Check if list A elements are exist in list B elements while preserving the order
    returns: True if A in B, False otherwise.
    """
    if len(a) > len(b):
        return False
    elif len(a) == len(b):
        return a == b
    else:
        for seq_start in range(len(b) - len(a) + 1):
            contains_flag = True
            for n in range(len(a)):
                if a[n] != b[seq_start + n]:
                    contains_flag = False
                    break
            if contains_flag:
                return True

        return False


def list_a_in_b_similar(a: list, b: list, tolerance: int):
    """
    Check if list A elements are exist in list B elements while preserving the order
    a: The first list where a belong to b and should preserve the order
    b: The second container list where a should exist in b while preserving the order
    tolerance: The tolerance value on each term such that a in b when b = [a[n] +- tol, a[n+1] +- tol, ... etc]
    returns: True if A in [B +- tolerance], False otherwise.
    """
    if len(a) > len(b):
        return False
    elif len(a) == len(b):
        return a == b
    else:
        for seq_start in range(len(b) - len(a) + 1):
            contains_flag = True
            for n in range(len(a)):
                if a[n] > b[seq_start + n] + tolerance or a[n] < b[seq_start + n] - tolerance:
                    contains_flag = False
                    break
            if contains_flag:
                return True

        return False


def search_and_echo(sequence_after_applying_operation: str, current_value: int = 0, echo_string: str = ""):
    """
    A function that is used by the advanced search operations
    returns: nothing
    """
    # Search
    returned_list = eng.ordered_search(sequence_after_applying_operation)

    # Echo Sequence
    if echo_string != "":
        print("[+] Current " + echo_string + ": " + str(current_value))

    # Echo Results
    print("    Current Seq ---> " + sequence_after_applying_operation)
    if len(returned_list) == 0:
        print("    Results ---> Nothing Found", end='')
    else:
        print("    Results ---> ", end='')
        for d in range(0, len(returned_list)):
            print(returned_list[d][0:returned_list[d].find(',')], end='')

    # Done
    print("\n[#]")


def waiting(index: int, over_all: int):
    # Progress ...
    perc = round(index / over_all * 100, 2)
    if index % 4 == 0:
        print("---> [//] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 1:
        print("---> [--] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 2:
        print("---> [\\\\] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 3:
        print("---> [||] ---> (" + str(perc) + "%)", end='\r')


########################################################################################################################
########################################################################################################################
print("[+] Data Loading ... Please Wait ...")

# Definitions
seq_list: list
seq_list_numeric: list

# Loading Strings
with open("data/stripped") as f:
    seq_list = f.readlines()
del seq_list[0:4]

# Loading Integers
seq_list_numeric = [[0]] * len(seq_list)
for i in range(len(seq_list)):
    seq_list_numeric[i] = convert_str_to_list(seq_list[i])

print("[+] Data Loading is Done Successfully ...")
########################################################################################################################
########################################################################################################################

"""
def load_numeric_sequence_list():
    global seq_list_numeric
    if len(seq_list_numeric) != 0:
        return
"""
