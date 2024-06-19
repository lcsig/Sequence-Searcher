#!/bin/env python3
import importlib
import signal
import sys
import urllib.request
import readline

import operation
import search_engine
from utils import *


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
_SEP = "[#]"
_YOUR_CHOICE = "[-] Your choice: "
_ENTER_YOUR_SEQ = "[-] Enter your sequence (Comma Seperated - Enter to use the last input): "
_ENTER_YOUR_SEQ_NAME = "[-] Enter the sequence number: "
_SEQ_AT_INDEX = "Sequence @ Index of Term that has Matched"
########################################################################################################################
_SHOULD_NOT_CONTAINS_PATTERN = "[!] The sequence should not contain anything but numbers!\n[#]"
_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST = "[!] The sequence should contain one number at least!\n[#]"
_CANT_IDENTIFY_THE_SEQUENCE = '[!] Please, enter the sequence again.\n[#]'
_CANT_IDENTIFY_THE_CHOICE = '[!] Please, enter your choice again.\n[#]'
_MAX_GAP_SIZE_BIGGER_THAN_ALLOWED_TERM = "[!] The gap size is bigger than the number of terms that can be dropped.\n[#]"
_ERR_OCCURRED_TRY_EXCEPTION = "[!] An error occurred, probably your input was not valid!"
########################################################################################################################


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
    seq = seq.replace(";", ",")
    if "," in seq:
        seq = seq.replace(" ", "").strip().strip(",")
        seq = ','.join(list(filter(None, seq.split(",")))).strip().strip(",")
    else:
        seq = ' '.join(seq.strip().split()).replace(" ", ",")
    return seq


def sep():
    print(_SEP)


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


def does_sequence_have_formula(sequence_number: str) -> bool:
    """
    This function will return True if the 'formula' section is exist in OEIS website for a specific sequence
    sequence_number: The sequence number (e.g. A0125)
    """
    oeis_url = f"https://oeis.org/{sequence_number}"

    with urllib.request.urlopen(oeis_url) as url_data:
        html_page = url_data.read().decode("utf8")

    return "FORMULA" in html_page


def get_numbers_indices(oeis_seq: str, input_seq: str) -> str:
    oeis_seq = search_engine.convert_str_to_list(oeis_seq, True, True)
    input_seq = search_engine.convert_str_to_list(input_seq, True, False)
    indices = ""
    
    last_index = -1
    for i in range(len(input_seq)):

        indices_updated = False
        for n in range(last_index + 1, len(oeis_seq)):
            if oeis_seq[n] == input_seq[i]:
                indices += str(n) + ", "
                last_index = n
                indices_updated = True
                break
        if not indices_updated:
            indices += "?1, "

    return indices.strip().strip(",")


def search_shift_with_constant(seq: str, max_constant: int):
    """
    Shift The Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one of them will be added each time to the sequence
    returns: nothing
    """
    numeric_seq = search_engine.convert_str_to_list(seq, True, False)
    for i in range(-1 * max_constant, max_constant + 1):
        # Calculate the Sequence
        string_seq_shifted = [x + i for x in numeric_seq]
        string_seq_shifted = ','.join(str(x) for x in string_seq_shifted)
        returned_list = search_engine.ordered_search(string_seq_shifted)

        if len(returned_list) > 0:
            print(f"    Current Seq ({i}) ---> " + string_seq_shifted)
            print(f"    Results ---> ", end='')
            for d in range(0, len(returned_list)):
                print(returned_list[d][0:returned_list[d].find(',')], end='')
            print()


def print_ranked_results_with_indices(returned_values: dict, terms_allowed_dropped: int, seq_input: str,
                                      n_terms_from_indices_begin: int, search_about_n_terms_from_indices_end: int):

    for i in range(terms_allowed_dropped, -1, -1):
        if i in returned_values.keys():
            print("[+] Rank: " + str(i))

            seq_list = returned_values[i]
            for n in range(0, len(seq_list)):
                seq_name = search_engine.get_sequence_name(seq_list[n])
                indices = get_numbers_indices(seq_list[n], seq_input)
                print(f"{seq_name} --{'OK' if does_sequence_have_formula(seq_name) else '--'}--> " + indices)

                numeric_seq = search_engine.convert_str_to_list(indices, True, False)
                if not (search_about_n_terms_from_indices_end == -1 or n_terms_from_indices_begin == -1):
                    search_about_n_terms_from_indices_end += 1
                    numeric_seq = numeric_seq[n_terms_from_indices_begin:search_about_n_terms_from_indices_end]
                max_shift_constant = 2 if (-2 <= numeric_seq[0] <= 2) else numeric_seq[0]

                search_shift_with_constant(','.join(str(x) for x in numeric_seq), max_shift_constant)

        else:
            print("[+] No matches for rank " + str(i))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    old_sequence = ''

    while True:
        try:
            echo_main()
            choice = input(_YOUR_CHOICE).strip()
            if not choice.isdigit() or (int(choice) < 0 or int(choice) > 6):
                print(_CANT_IDENTIFY_THE_CHOICE)
                continue
            if choice == '0':
                seq_number = input(_ENTER_YOUR_SEQ_NAME)
                seq_number = int(seq_number.strip("A"))
                sep()
                print(search_engine.get_sequence_name_by_number(seq_number))
                print(search_engine.get_sequence_terms_by_number(seq_number))
                sep()
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
            if (choice == '1' or choice == '3' or choice == '5' or choice == '6') \
                    and not are_all_terms_fixed_numbers(seq_input):
                print(_SHOULD_NOT_CONTAINS_PATTERN)
                print(_CANT_IDENTIFY_THE_SEQUENCE)
                continue
            elif choice == '2' and not does_seq_contain_fixed_numbers(seq_input):
                print(_MUST_CONTAIN_ONE_FIXED_NUMBER_AT_LEAST)
                continue
            elif choice == '4' and ('n,' not in seq_input.lower() or ',n' not in seq_input.lower()):
                print(_CANT_IDENTIFY_THE_SEQUENCE)
                continue


            # Evaluate Search Criteria Based on Input
            if choice == '1':
                allowed_drop = int(input(_NUMBER_OF_ALLOWED_DROP))
                ret = search_engine.unordered_search(seq_input, allowed_drop)
                sep()
                print_ranked_results(ret, allowed_drop)
                sep()
                continue


            elif choice == '2':
                ret = search_engine.ordered_search(seq_input)
                sep()
                print_results(ret)
                sep()
                continue


            elif choice == '3':
                echo_fuzzy_matching()
                choice = input(_YOUR_CHOICE).strip()
                if not (choice.upper() == "IV" or choice == "4"):
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

                elif choice.upper() == "IV" or choice == "4":                       # Undocumented
                    begin_indices = input("[+] Enter the beginning of searching range for indices terms (Enter to skip): ")
                    if begin_indices.strip() == "":
                        begin_indices = -1
                        end_indices = -1
                    else:
                        begin_indices = int(begin_indices)
                        end_indices = input("[+] Enter the ending of searching range for indices terms: ")
                        end_indices = int(end_indices)

                    begin_shifting_range = int(input("[+] Enter the beginning of shifting range for the input seq: "))
                    end_shifting_range = int(input("[+] Enter the ending of shifting range for the input seq: "))

                    numeric_seq = search_engine.convert_str_to_list(seq_input, True, False)
                    for i in range(begin_shifting_range, end_shifting_range + 1):
                        string_seq_shifted = [x + i for x in numeric_seq]
                        string_seq_shifted = ','.join(str(x) for x in string_seq_shifted)

                        print(f"[+] Search About (seq({i})): " + string_seq_shifted)
                        ret = search_engine.fuzzy_match_type3(string_seq_shifted, 0)

                        print_ranked_results_with_indices(ret, 0, string_seq_shifted, begin_indices, end_indices)

                    continue
                else:
                    continue

                sep()
                print_ranked_results(ret, allowed_drop)
                sep()
                continue


            elif choice == '4':
                ret = search_engine.formula_lookup(seq_input)
                matched_sequences, matched_term_index = list(ret.keys()), list(ret.values())

                if len(matched_sequences) > 0:
                    print(_SEQ_AT_INDEX)
                for i in range(len(matched_sequences)):
                    print(search_engine.get_sequence_name(matched_sequences[i]) + " @ " + str(matched_term_index[i]))
                sep()
                continue


            elif choice == '5':
                advanced_search()
                sep()
                continue


            elif choice == '6':
                input("[-] Please, Edit The 'operation.py' File and Press Enter When You Ready ...")
                importlib.invalidate_caches()
                k = importlib.reload(operation)
                ret = search_engine.operation_design(operation.oeis_transform,
                                                     operation.input_transform,
                                                     operation.filter_fun,
                                                     seq_input)
                sep()
                print_results(ret)
                sep()
                continue


        except SystemExit:
            signal_handler(None, None)
        except KeyboardInterrupt:
            signal_handler(None, None)
        except Exception as err:
            sep()
            print(_ERR_OCCURRED_TRY_EXCEPTION)
            sep()
