import search_engine.seq as utils
import search_engine.seq_calc as utils_calc

"""
Contains:
12. Search About Similar Sequence
13. Check if the Sequence is The Summation of Two Sequences
14. Check if The Sequence is The Product of Two Sequences
"""

from search_engine import seq_list_numeric
from search_engine import seq_list
from search_engine import get_sequence_name


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


def adv_search_find_similar(seq: str, tolerance_value: int):
    """
    Search About Similar Sequence by Setting a Tolerance Value on Each Term in The Sequence
    seq: A string that contains a comma seperated numbers
    tolerance_value: A tolerance value where each term could be -+tolerance_value
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        if list_a_in_b_similar(numeric_seq, seq_list_numeric[i], tolerance_value):
            result_list.append(get_sequence_name(seq_list[i]))

        utils.waiting(i, len(seq_list_numeric))

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print(result_list[i])


def two_sum_hashes(num_list: list, target_sum: int):
    """
    This method solves the two sum problem in linear time
    num_list: List of integers where we need to find two numbers in this list that have a summation of target_sum
    target_sum: The target summation where num_list[x] + num_list[y] = target_sum
    returns: List of set of integers where each set contains two indices for the num_list where
        num_list[x] + num_list[y] = target_sum
    """
    sums = []
    hashTable = {}
    hashTable2 = {}

    for i in range(len(num_list)):
        complement = target_sum - num_list[i]
        if complement in hashTable:
            print("Pair with sum", target_sum, "is: (", num_list[i], ",", complement, ")")
            hashTable2[num_list[i]] = complement

        hashTable[num_list[i]] = num_list[i]

    print(hashTable2)


def adv_search_summation_of_two_seq(seq: str):
    """
    Check If the Sequence is The Summation of Two Sequences
    seq: A string that contains a comma seperated numbers
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    seq_len = len(seq_list_numeric)
    for i in range(0, seq_len):
        for n in range(i + 1, seq_len):
            seq_result = utils_calc.add_sequences(seq_list_numeric[i], seq_list_numeric[n])
            if utils.list_a_in_b(numeric_seq, seq_result):
                result_list.append([get_sequence_name(seq_list[i]), get_sequence_name(seq_list[n])])

        # Progress ...
        utils.waiting(i, seq_len)

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print(result_list[i][0] + " <--> " + result_list[i][1])


def adv_search_product_of_two_seq(seq: str):
    """
    Check If the Sequence is The Product of Two Sequences
    seq: A string that contains a comma seperated numbers
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        for n in range(i + 1, len(seq_list_numeric)):
            seq_result = utils_calc.multiply_sequences(seq_list_numeric[i], seq_list_numeric[n])
            if utils.list_a_in_b(numeric_seq, seq_result):
                result_list.append([get_sequence_name(seq_list[i]), get_sequence_name(seq_list[n])])

        # Progress ...
        utils.waiting(i, len(seq_list_numeric))

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print(result_list[i][0] + " <--> " + result_list[i][1])
