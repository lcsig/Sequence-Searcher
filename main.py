#!/bin/env python3

import search_engine
from utils import *
import signal
import sys

########################################################################################################################
_MAX_SHIFT_VALUE_N_TO_N = "[-] Maximum constant value (Values from -constant to +constant will be applied): "
_MAX_N_VALUE_N_TO_N = "[-] Maximum N value (Values from -N to N will be applied): "
_MAX_LEVEL_VALUE = "[-] Enter the maximum level (Levels from 1 to the maximum level will be applied): "
_PRIME_START_POINT = "[-] The starting point of primes sequence: "
_PRIME_END_POINT = "[-] The ending point of primes sequence: "
_TOLERANCE_VALUE = "[-] Tolerance Value (Each term will have a tolerance of +- the entered value): "
_NUMBER_OF_ALLOWED_DROP = "[-] Number of allowed terms to be dropped: "
_TERMS_LOOKUP_FORMULA = "[-] Enter your terms lookup formula using only 'n' (E.g., n / 5, n, n * 10, n * 10 + 125): "
_MAXIMUM_GAP_SIZE = "[-] Enter your maximum gap size: "
########################################################################################################################
_YOUR_CHOICE = "[-] Your choice: "
_ENTER_YOUR_SEQ = "[-] Enter your sequence (comma seperated): "
########################################################################################################################
_SHOULD_NOT_CONTAINS_PATTERN = "[!] The sequence should not contain anything but numbers!\n[#]"
_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST = "[!] The sequence should contain one number at least!\n[#]"
_CANT_IDENTIFY_THE_SEQUENCE = '[!] Please, enter the sequence again.\n[#]'
_CANT_IDENTIFY_THE_CHOICE = '[!] Please, enter your choice again.\n[#]'
_MAX_GAP_SIZE_BIGGER_THAN_ALLOWED_TERM = "[!] The gap size is bigger than the number of terms that can be dropped.\n[#]"


def signal_handler(sig, frame):
    print('\n[!] ...')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    old_sequence = ''

    while True:
        echo_main()
        choice = input(_YOUR_CHOICE).strip()
        if not choice.isdigit() or (int(choice) < 1 or int(choice) > 5):
            print(_CANT_IDENTIFY_THE_CHOICE)
            continue


        if choice == '4':
            terms_lookup_formula = input(_TERMS_LOOKUP_FORMULA)
            ret = search_engine.formula_lookup(terms_lookup_formula)
            matched_sequences, matched_term_index = list(ret.keys()), list(ret.values())

            if len(matched_sequences) > 0:
                print("Sequence @ Index of Term that has Matched")
            for i in range(len(matched_sequences)):
                print(get_sequence_name(matched_sequences[i]) + " @ " + str(matched_term_index[i]))
            continue


        # Echo Based on Input
        if choice == '2':
            echo_syntax()
        elif choice == '5':
            echo_advanced()


        # Sequence Input and Validation
        seq_input = input(_ENTER_YOUR_SEQ).replace(";", ",")
        if seq_input.strip() == '':
            seq_input = old_sequence
            print("[+] Seq: " + seq_input)

        if ',' not in seq_input and ' ' not in seq_input.strip():
            print(_CANT_IDENTIFY_THE_SEQUENCE)
            continue
        elif ',' not in seq_input and ' ' in seq_input.strip():
            seq_input = ' '.join(seq_input.strip().split()).replace(" ", ",")
            print("[+] Seq: " + seq_input)
        old_sequence = seq_input


        # Validate Input Based on Choice
        if (choice == '1' or choice == '3' or choice == '5') and not is_all_terms_are_fixed_numbers(seq_input):
            print(_SHOULD_NOT_CONTAINS_PATTERN)
            print(_CANT_IDENTIFY_THE_SEQUENCE)
            continue
        elif choice == '2' and not is_seq_contains_fixed_numbers(seq_input):
            print(_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST)
            continue


        # Evaluate Based on Input
        if choice == '1':
            ret = search_engine.unordered_search(seq_input)
            print_ret(ret)


        elif choice == '2':
            ret = search_engine.ordered_search(seq_input)
            print_ret(ret)


        elif choice == '3':
            echo_fuzzy_matching()
            choice = input(_YOUR_CHOICE).strip()
            allowed_drop = int(input(_NUMBER_OF_ALLOWED_DROP))

            if choice.upper() == "I" or choice == "1":
                ret = search_engine.fuzzy_match_type1(seq_input, allowed_drop)
            elif choice.upper() == "II" or choice == "2":
                max_gap_size = int(input(_MAXIMUM_GAP_SIZE))
                if max_gap_size > allowed_drop:
                    print(_MAX_GAP_SIZE_BIGGER_THAN_ALLOWED_TERM)
                    continue
                ret = search_engine.fuzzy_match_type2(seq_input, allowed_drop, max_gap_size)
            elif choice.upper() == "III" or choice == "3":
                continue
            else:
                continue

            print("[#]")
            for i in range(allowed_drop, -1, -1):
                if i in ret.keys():
                    print("[+] Rank: " + str(i))
                    print_ret(ret[i])
                else:
                    print("[+] No matches for rank " + str(i))


        elif choice == '5':
            choice = input(_YOUR_CHOICE)
            ############################################################################################################
            if choice == '1':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                search_engine.adv_search_shift_constant(seq_input, int(range_param))
                pass

            elif choice == '2':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                search_engine.adv_search_scale_constant(seq_input, int(range_param))
                pass

            elif choice == '3':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                search_engine.adv_search_shift_n(seq_input, int(range_param))
                pass

            elif choice == '4':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                search_engine.adv_search_scale_n(seq_input, int(range_param))
                pass

            elif choice == '5':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                search_engine.adv_search_shift_and_scale_constant(seq_input, int(range_param))
                pass

            elif choice == '6':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                search_engine.adv_search_shift_and_scale_n(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '7':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_adjacent_terms_difference(seq_input, int(range_param))
                pass

            elif choice == '8':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_adjacent_terms_sum(seq_input, int(range_param))
                pass

            elif choice == '9':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_adjacent_terms_product(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '10':
                prime_start = input(_PRIME_START_POINT)
                prime_end = input(_PRIME_END_POINT)
                search_engine.adv_search_primes_shift(seq_input, int(prime_start), int(prime_end))
                pass

            elif choice == '11':
                prime_start = input(_PRIME_START_POINT)
                prime_end = input(_PRIME_END_POINT)
                search_engine.adv_search_primes_scale(seq_input, int(prime_start), int(prime_end))
                pass
            ############################################################################################################
            elif choice == '12':
                shift_tolerance = input(_TOLERANCE_VALUE)
                search_engine.adv_search_find_similar(seq_input, int(shift_tolerance))
                pass

            elif choice == '13':
                search_engine.adv_search_summation_of_two_seq(seq_input)
                pass

            elif choice == '14':
                search_engine.adv_search_product_of_two_seq(seq_input)
                pass
            ############################################################################################################
            elif choice == '15':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_cumulative_sum(seq_input, int(range_param))
                pass

            elif choice == '16':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_cumulative_product(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '17':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_differences(seq_input, int(range_param))
                pass

            elif choice == '18':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_sums(seq_input, int(range_param))
                pass

            elif choice == '19':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_products(seq_input, int(range_param))
                pass

            elif choice == '20':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_cumulative_sum(seq_input, int(range_param))
                pass

            elif choice == '21':
                range_param = input(_MAX_LEVEL_VALUE)
                search_engine.adv_search_cumulative_product(seq_input, int(range_param))
                pass
            ############################################################################################################
