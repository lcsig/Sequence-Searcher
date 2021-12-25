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
_NUMBER_OF_ALLOWED_DROP = "[-] Number of terms allowed to be dropped: "
_TERMS_LOOKUP_FORMULA = "[-] Enter your terms lookup formula using only 'n' (E.g., n / 5, n, n * 10, n * 10 + 125): "
_MAXIMUM_GAP_SIZE = "[-] Enter your maximum gap size: "
########################################################################################################################
_YOUR_CHOICE = "[-] Your choice: "
_ENTER_YOUR_SEQ = "[-] Enter your sequence (Comma Seperated - Enter to use the last input): "
_ENTER_YOUR_SEQ_NAME = "[-] Enter the sequence number: "
########################################################################################################################
_SHOULD_NOT_CONTAINS_PATTERN = "[!] The sequence should not contain anything but numbers!\n[#]"
_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST = "[!] The sequence should contain one number at least!\n[#]"
_CANT_IDENTIFY_THE_SEQUENCE = '[!] Please, enter the sequence again.\n[#]'
_CANT_IDENTIFY_THE_CHOICE = '[!] Please, enter your choice again.\n[#]'
_MAX_GAP_SIZE_BIGGER_THAN_ALLOWED_TERM = "[!] The gap size is bigger than the number of terms that can be dropped.\n[#]"


def signal_handler(sig, frame):
    print('\r[!] .......                                                                                              ')
    sys.exit(0)


def print_results(returned_list: list):
    if len(returned_list) == 0:
        print("[!] Could not find any results!")
    else:
        for i in range(0, len(returned_list)):
            print(search_engine.get_sequence_name(returned_list[i]))


def print_ranked_results(returned_values: dict, terms_allowed_dropped: int):
    for i in range(terms_allowed_dropped, -1, -1):
        if i in returned_values.keys():
            print("[+] Rank: " + str(i))
            print_results(returned_values[i])
        else:
            print("[+] No matches for rank " + str(i))


def clear_input(seq: str):
    seq = seq.replace(";", ",").replace(":", ",")
    if "," in seq:
        seq = seq.replace(" ", "").strip().strip(",")
        seq = ','.join(list(filter(None, seq.split(",")))).strip().strip(",")
    else:
        seq = ' '.join(seq.strip().split()).replace(" ", ",")
    return seq


def advanced_search():
    choice = input(_YOUR_CHOICE)

    if choice == '1':
        range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
        search_engine.adv_search_shift_constant(seq_input, int(range_param))
    elif choice == '2':
        range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
        search_engine.adv_search_scale_constant(seq_input, int(range_param))
    elif choice == '3':
        range_param = input(_MAX_N_VALUE_N_TO_N)
        search_engine.adv_search_shift_n(seq_input, int(range_param))
    elif choice == '4':
        range_param = input(_MAX_N_VALUE_N_TO_N)
        search_engine.adv_search_scale_n(seq_input, int(range_param))
    elif choice == '5':
        range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
        search_engine.adv_search_shift_and_scale_constant(seq_input, int(range_param))
    elif choice == '6':
        range_param = input(_MAX_N_VALUE_N_TO_N)
        search_engine.adv_search_shift_and_scale_n(seq_input, int(range_param))
    ############################################################################################################
    elif choice == '7':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_adjacent_terms_difference(seq_input, int(range_param))
    elif choice == '8':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_adjacent_terms_sum(seq_input, int(range_param))
    elif choice == '9':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_adjacent_terms_product(seq_input, int(range_param))
    ############################################################################################################
    elif choice == '10':
        prime_start = input(_PRIME_START_POINT)
        prime_end = input(_PRIME_END_POINT)
        search_engine.adv_search_primes_shift(seq_input, int(prime_start), int(prime_end))
    elif choice == '11':
        prime_start = input(_PRIME_START_POINT)
        prime_end = input(_PRIME_END_POINT)
        search_engine.adv_search_primes_scale(seq_input, int(prime_start), int(prime_end))
    ############################################################################################################
    elif choice == '12':
        shift_tolerance = input(_TOLERANCE_VALUE)
        search_engine.adv_search_find_similar(seq_input, int(shift_tolerance))
    elif choice == '13':
        search_engine.adv_search_summation_of_two_seq(seq_input)
    elif choice == '14':
        search_engine.adv_search_product_of_two_seq(seq_input)
    ############################################################################################################
    elif choice == '15':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_cumulative_sum(seq_input, int(range_param))
    elif choice == '16':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_cumulative_product(seq_input, int(range_param))
    ############################################################################################################
    elif choice == '17':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_differences(seq_input, int(range_param))
    elif choice == '18':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_sums(seq_input, int(range_param))
    elif choice == '19':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_products(seq_input, int(range_param))
    elif choice == '20':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_cumulative_sum(seq_input, int(range_param))
    elif choice == '21':
        range_param = input(_MAX_LEVEL_VALUE)
        search_engine.adv_search_cumulative_product(seq_input, int(range_param))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    old_sequence = ''

    while True:
        try:
            echo_main()
            choice = input(_YOUR_CHOICE).strip()
            if not choice.isdigit() or (int(choice) < 0 or int(choice) > 5):
                print(_CANT_IDENTIFY_THE_CHOICE)
                continue
            if choice == '0':
                seq_number = input(_ENTER_YOUR_SEQ_NAME)
                seq_number = int(seq_number.strip("A"))
                print("[#]")
                print(search_engine.get_sequence_name_by_number(seq_number))
                print(search_engine.get_sequence_terms_by_number(seq_number))
                print("[#]")
                continue


            # Echo Before Input Based on Choice
            if choice == '2':
                echo_syntax()
            elif choice == '5':
                echo_advanced()


            # Sequence Input and Checking
            seq_input = clear_input(input(_ENTER_YOUR_SEQ if choice != '4' else _TERMS_LOOKUP_FORMULA))
            seq_input = old_sequence if seq_input.strip() == '' else seq_input.strip()

            if ',' not in seq_input:
                print(_CANT_IDENTIFY_THE_SEQUENCE)
                continue
            else:
                print("[+] Seq: " + seq_input)
                old_sequence = ' '.join(seq_input.split())


            # Validate Input Based on Choice
            if (choice == '1' or choice == '3' or choice == '5') and not is_all_terms_are_fixed_numbers(seq_input):
                print(_SHOULD_NOT_CONTAINS_PATTERN)
                print(_CANT_IDENTIFY_THE_SEQUENCE)
                continue
            elif choice == '2' and not is_seq_contains_fixed_numbers(seq_input):
                print(_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST)
                continue
            elif choice == '4' and ('n,' not in seq_input.lower() or ',n' not in seq_input.lower()):
                print(_CANT_IDENTIFY_THE_SEQUENCE)
                continue


            # Evaluate Search Criteria Based on Input
            if choice == '1':
                allowed_drop = int(input(_NUMBER_OF_ALLOWED_DROP))
                ret = search_engine.unordered_search(seq_input, allowed_drop)
                print("[#]")
                print_ranked_results(ret, allowed_drop)
                print("[#]")
                continue


            elif choice == '2':
                ret = search_engine.ordered_search(seq_input)
                print("[#]")
                print_results(ret)
                print("[#]")
                continue


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
                    ret = search_engine.fuzzy_match_type3(seq_input, allowed_drop)
                else:
                    continue

                print("[#]")
                print_ranked_results(ret, allowed_drop)
                print("[#]")
                continue


            elif choice == '4':
                ret = search_engine.formula_lookup(seq_input)
                matched_sequences, matched_term_index = list(ret.keys()), list(ret.values())

                if len(matched_sequences) > 0:
                    print("Sequence @ Index of Term that has Matched")
                for i in range(len(matched_sequences)):
                    print(search_engine.get_sequence_name(matched_sequences[i]) + " @ " + str(matched_term_index[i]))
                print("[#]")
                continue


            elif choice == '5':
                advanced_search()
                print("[#]")
                continue


        except SystemExit:
            signal_handler(None, None)
        except KeyboardInterrupt:
            signal_handler(None, None)
        except Exception as err:
            print("[#]")
            print("[!] An error occurred, probably your input was not valid!")
            print("[#]")
