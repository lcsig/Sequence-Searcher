from search_engine import seq_list_numeric
from search_engine import convert_str_to_list
from search_engine import seq_list
import search_engine.utils as utils

"""
This file contains the implementations for fuzzy match algorithm
"""


def fuzzy_match_two_seq_t1(seq1: list, seq2: list, max_off_terms: int):
    """
    returns: The number of remaining terms to drop, Otherwise -1 is returned.
    """
    seq1_idx, seq2_idx = 0, 0

    while True:

        if seq2_idx > len(seq2) - 1:
            return max_off_terms
        elif seq1_idx > len(seq1) - 1 and max_off_terms > len(seq2) - 1 - seq2_idx:
            return max_off_terms - ((len(seq2) - 1) - (seq2_idx - 1))
        elif seq1_idx > len(seq1) - 1:
            return -1

        if seq1[seq1_idx] == seq2[seq2_idx]:
            seq1_idx, seq2_idx = seq1_idx + 1, seq2_idx + 1
            continue
        else:
            if max_off_terms == 0:
                return -1
            max_off_terms = max_off_terms - 1

            # Avoid out of index error
            if seq2_idx + 1 >= len(seq2) or seq1_idx + 1 >= len(seq1):
                return -1

            if seq1[seq1_idx] == seq2[seq2_idx + 1]:
                seq2_idx = seq2_idx + 1
            elif seq1[seq1_idx + 1] == seq2[seq2_idx]:
                seq1_idx = seq1_idx + 1
            elif seq1[seq1_idx + 1] == seq2[seq2_idx + 1]:
                seq1_idx, seq2_idx = seq1_idx + 1, seq2_idx + 1
                continue
            else:
                return -1


def fuzzy_match_type1(num_list: str, max_off_terms: int):
    """
    This function will match a target sequence with the database while taking into consideration that the sequence
        may not contain some terms.
    num_list: The sequence that you are looking for
    max_off_terms: The maximum number of terms that are allowed to be dropped off while searching
    returns: A dictionary where the key value represents the rank and the dictionary value represents a list of the
        matched sequences
    """
    seq2 = convert_str_to_list(num_list, True, False)
    return_dic = {}

    for i in range(len(seq_list_numeric)):
        seq1 = seq_list_numeric[i]
        # if str(seq_list[i]).startswith('A348440'):
        #     print("debug")
        dropped_terms = []
        for n in range(len(seq1) - len(seq2) + max_off_terms + 1):
            seq1_cut = seq1[n:]
            rank = fuzzy_match_two_seq_t1(seq1_cut, seq2, max_off_terms)
            if rank != -1:
                dropped_terms.append(rank)

        # Sort and Reverse to take the best rank found in the sequence
        if len(dropped_terms) > 0:
            dropped_terms.sort()
            dropped_terms.reverse()
            dropped_terms = dropped_terms[0]
            return_dic.setdefault(dropped_terms, []).append(seq_list[i])

        utils.waiting(i, len(seq_list_numeric))

    return return_dic


def fuzzy_match_two_seq_t2(seq1: list, seq2: list, max_off_terms: int, max_gap_size: int):
    """
    returns: The number of remaining terms to drop, Otherwise -1 is returned.
    """
    seq1_idx, seq2_idx = 0, 0

    while True:

        if seq2_idx > len(seq2) - 1:
            return max_off_terms
        elif seq1_idx > len(seq1) - 1 \
                and max_off_terms > len(seq2) - 1 - seq2_idx \
                and max_gap_size > len(seq2) - 1 - seq2_idx:
            return max_off_terms - ((len(seq2) - 1) - (seq2_idx - 1))
        elif seq1_idx > len(seq1) - 1:
            return -1

        if seq1[seq1_idx] == seq2[seq2_idx]:
            seq1_idx, seq2_idx = seq1_idx + 1, seq2_idx + 1
            continue
        else:
            i_gap_range = max_gap_size if seq1_idx + max_gap_size < len(seq1) else len(seq1) - seq1_idx - 1
            n_gap_range = max_gap_size if seq2_idx + max_gap_size < len(seq2) else len(seq2) - seq2_idx - 1

            break_flag = False
            for i_gap in range(0, i_gap_range + 1):
                for n_gap in range(0, n_gap_range + 1):
                    if seq1[seq1_idx + i_gap] == seq2[seq2_idx + n_gap]:
                        seq1_idx, seq2_idx = seq1_idx + i_gap, seq2_idx + n_gap

                        if i_gap != 0 and n_gap != 0:
                            max_off_terms = max_off_terms - (i_gap if i_gap <= n_gap else n_gap)  # To be specified ...
                        else:
                            max_off_terms = max_off_terms - (i_gap if i_gap >= n_gap else n_gap)

                        break_flag = True
                        break
                if break_flag:
                    break

            # If the break is false, then there is no match between the next two parts of the sequences
            if not break_flag:
                return -1

            # If the number of the terms allowed to be dropped is below zero
            if max_off_terms < 0:
                return -1

            if i_gap_range == 0 or n_gap_range == 0:
                return -1


def fuzzy_match_type2(num_list: str, max_off_terms: int, max_gap_size: int):
    """
    This function will match a target sequence with the database while taking into consideration that the sequence
        may not contain some terms.
    num_list: The sequence that you are looking for
    max_off_terms: The maximum number of terms that are allowed to be dropped off while searching
    max_gap_size: The maximum number of terms that can be dropped at a time.
    returns: A dictionary where the key value represents the rank and the dictionary value represents a list of the
        matched sequences
    """
    seq2 = convert_str_to_list(num_list, True, False)
    return_dic = {}

    for i in range(len(seq_list_numeric)):
        seq1 = seq_list_numeric[i]
        # if str(seq_list[i]).startswith('A333516'):
        #    print("debug")
        dropped_terms = []
        for n in range(len(seq1) - len(seq2) + max_off_terms + 1):
            seq1_cut = seq1[n:]
            rank = fuzzy_match_two_seq_t2(seq1_cut, seq2, max_off_terms, max_gap_size)
            if rank != -1:
                dropped_terms.append(rank)

        # Sort and Reverse to take the best rank found in the sequence
        if len(dropped_terms) > 0:
            dropped_terms.sort()
            dropped_terms.reverse()
            dropped_terms = dropped_terms[0]
            return_dic.setdefault(dropped_terms, []).append(seq_list[i])

        utils.waiting(i, len(seq_list_numeric))

    return return_dic


def fuzzy_match_two_seq_t3(seq1: list, seq2: list, max_off_terms: int):
    """
    returns: The number of remaining terms to drop, Otherwise -1 is returned.
    """

    seq1_idx, seq2_idx = 0, 0
    while True:
        if max_off_terms < 0:
            return -1
        if seq2_idx > len(seq2) - 1:
            return max_off_terms
        if seq1_idx > len(seq1) - 1 and max_off_terms >= len(seq2) - seq2_idx:
            return max_off_terms - ((len(seq2) - 1) - (seq2_idx - 1))
        if seq1_idx > len(seq1) - 1:
            return -1

        if seq2[seq2_idx] not in seq1[seq1_idx:]:
            seq1_idx -= 0
            seq2_idx += 1
            max_off_terms -= 1

        elif seq2[seq2_idx] in seq1[seq1_idx:]:
            seq1_idx = seq1_idx + seq1[seq1_idx:].index(seq2[seq2_idx]) + 1
            seq2_idx += 1
            max_off_terms -= 0


def fuzzy_match_type3(num_list: str, max_off_terms: int):
    """
    This function will match a target sequence with the database while taking into consideration that the sequence
        may not contain some terms.
    num_list: The sequence that you are looking for
    max_off_terms: The maximum number of terms that are allowed to be dropped off while searching
    returns: A dictionary where the key value represents the rank and the dictionary value represents a list of the
        matched sequences
    """
    seq2 = convert_str_to_list(num_list, True, False)
    return_dic = {}

    for i in range(len(seq_list_numeric)):
        seq1 = seq_list_numeric[i]
        # if str(seq_list[i]).startswith('A000027'):
        #    print("debug")
        dropped_terms = []
        for n in range(len(seq1) - len(seq2) + max_off_terms + 1):
            seq1_cut = seq1[n:]
            rank = fuzzy_match_two_seq_t3(seq1_cut, seq2, max_off_terms)
            if rank != -1:
                dropped_terms.append(rank)

        # Sort and Reverse to take the best rank found in the sequence
        if len(dropped_terms) > 0:
            dropped_terms.sort()
            dropped_terms.reverse()
            dropped_terms = dropped_terms[0]
            return_dic.setdefault(dropped_terms, []).append(seq_list[i])

        utils.waiting(i, len(seq_list_numeric))

    return return_dic