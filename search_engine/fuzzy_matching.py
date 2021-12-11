from search_engine import seq_list_numeric
from search_engine import convert_str_to_list
from search_engine import seq_list
import search_engine.seq as utils

"""
This file contains the implementations for fuzzy match algorithm
"""


def __fuzzy_match_two_seq(seq1: list, seq2: list, max_off_terms: int, max_gap_size: int):
    """
    returns: The number of remaining terms to drop, Otherwise -1 is returned.
    """
    i_shift, n_shift = 0, 0

    while True:

        if n_shift > len(seq2) - 1:
            return max_off_terms
        elif i_shift > len(seq1) - 1 and max_off_terms > len(seq2) - 1 - n_shift:
            return max_off_terms - (len(seq2) - 1 - n_shift)
        elif i_shift > len(seq1) - 1:
            return -1

        if seq1[i_shift] == seq2[n_shift]:
            i_shift, n_shift = i_shift + 1, n_shift + 1
            continue
        else:
            if max_off_terms == 0:
                return -1
            max_off_terms = max_off_terms - 1

            if n_shift + 1 >= len(seq2) or i_shift + 1 >= len(seq1):
                return -1

            if seq1[i_shift] == seq2[n_shift + 1]:
                n_shift = n_shift + 1
            elif seq1[i_shift + 1] == seq2[n_shift]:
                i_shift = i_shift + 1
            elif seq1[i_shift + 1] == seq2[n_shift + 1]:
                i_shift, n_shift = i_shift + 1, n_shift + 1
                continue
            else:
                return -1

    pass


def fuzzy_match(num_list: str, max_off_terms: int):
    """
    This function will match a target sequence with the database while taking into consideration that the sequence
        could not contain some terms.
    num_list: The sequence that you are looking for
    max_off_terms: The maximum number of terms that are allowed to be dropped off while searching
    """
    seq2 = convert_str_to_list(num_list, True, False)
    return_dic = {}

    for i in range(len(seq_list_numeric)):
        seq1 = seq_list_numeric[i]
        # if str(seq_list[i]).startswith('A348440'):
        #     print("debug")
        dropped_terms = []
        for n in range(len(seq1) - len(seq2) + max_off_terms):
            seq1_cut = seq1[n:]
            rank = __fuzzy_match_two_seq(seq1_cut, seq2, max_off_terms, 1)
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
