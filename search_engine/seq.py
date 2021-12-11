"""
This code contains a set of functions that will be used in the OEIS Search Engine
"""
import re


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


def print_percentage_line(index: int, perc: float):
    if index % 4 == 0:
        print("---> [//] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 1:
        print("---> [--] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 2:
        print("---> [\\\\] ---> (" + str(perc) + "%)", end='\r')
    elif index % 4 == 3:
        print("---> [||] ---> (" + str(perc) + "%)", end='\r')


def waiting(completed: int, over_all: int):
    perc = round(completed / over_all * 100, 2)
    print_percentage_line(completed, perc)


def waiting_with_index(index: int, completed: int, over_all: int):
    perc = round(completed / over_all * 100, 2)
    print_percentage_line(index, perc)


