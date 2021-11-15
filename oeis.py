#!/bin/env python

import modules.search_engine as eng
import modules.engine1 as eng1
import modules.engine2 as eng2
import modules.engine3 as eng3
import modules.engine4 as eng4
import modules.engine5 as eng5

import modules.seq as utils

_MAX_SHIFT_VALUE_N_TO_N = "[-] Maximum constant value (Values from -constant to +constant will be applied): "
_MAX_N_VALUE_N_TO_N = "[-] Maximum N value (Values from -N to N will be applied): "
########################################################################################################################
_MAX_LEVEL_VALUE = "[-] Enter the maximum level (Levels from 1 to the maximum level will be applied): "
_PRIME_START_POINT = "[-] The starting point of primes sequence: "
_PRIME_END_POINT = "[-] The ending point of primes sequence: "
_TOLERANCE_VALUE = "[-] Tolerance Value (Each term will have a tolerance of +- the entered value): "
########################################################################################################################
_YOUR_CHOICE = "[-] Your choice: "
_YOUR_SEQ = "[-] Enter your sequence (comma seperated): "
########################################################################################################################
_NO_PATTERN = "[!] The sequence should not contain anything but numbers!"
_ONE_NUMBER = "[!] The sequence should contain one number at least!"
_NOT_FOUND = "[!] Could not find any results!"


def echo_main():
    print("[+] 1. Search about set of numbers in a sequence.")
    print("[+] 2. Search about a sequence.")
    print("[+] 3. Advanced Search")
    pass


def echo_advanced():
    print("[+] 1. Shift The Sequence with Constant and Search")
    print("[+] 2. Scale The Sequence with Constant and Search")
    print("[+] 3. Shift The Sequence with (N, N+1, N+2 ..., N + length_of_sequence) and Search")
    print("[+] 4. Scale The Sequence with (N, N+1, N+2 ..., N + length_of_sequence) and Search")
    print("[+] 5. Scale and Shift The Sequence with Constant and Search")
    print("[+] 6. Scale and Shift The Sequence with (N, N+1, N+2 ..., N + length_of_sequence) and Search")
    ####################################################################################################################
    print("[+] 7. Search About Differences Between Adjacent Terms of The Input Sequence")
    print("[+] 8. Search About Sums Between Adjacent Terms of The Input Sequence")
    print("[+] 9. Search About Products Between Adjacent Terms of The Input Sequence")
    ####################################################################################################################
    print("[+] 10. Shift with Primes")
    print("[+] 11. Scale with Primes")
    ####################################################################################################################
    print("[+] 12. Search About Similar Sequence")
    print("[+] 13. Check If the Sequence is The Summation of Two Sequences (Too Much Time - Need Enhancement)")
    print("[+] 14. Check If the Sequence is The Product of Two Sequences (Too Much Time - Need Enhancement)")
    ####################################################################################################################
    print("[+] 15. Search About Cumulative Sums of The Input")
    print("[+] 16. Search About Cumulative Products of The Input")
    ####################################################################################################################
    print("[+] 17. Check if The Input is a Difference of a Sequence in The Database")
    print("[+] 18. Check if The Input is a Sum of Adjacent Terms of a Sequence in The Database")
    print("[+] 19. Check if The Input is a Product of Adjacent Terms of a Sequence in The Database")
    print("[+] 20. Check if The Input is a Cumulative Sum of a Sequence in The Database")
    print("[+] 21. Check if The Input is a Cumulative Product of a Sequence in The Database")
    ####################################################################################################################
    print("[+] A. Operation Design on Input (To Be Added Later)")
    print("[+] B. Operation Design on Database (To Be Added Later)")
    pass


def echo_syntax():
    print("[+] Reminder:")
    print("---> 1, ?3, 5, 7   ---> The second, third and forth sequences could be anything")
    print("---> 1, ?*, 18, 13 ---> Any number of terms between 1 and 100")
    print("---> 1, 2-5, 10-15 ---> The second term between 2 and 5, the third between 5 and 10")
    pass


def print_ret(returned_list: list):
    if len(returned_list) == 0:
        print(_NOT_FOUND)
    else:
        for i in range(0, len(returned_list)):
            print(returned_list[i][0:returned_list[i].find(',')])
            # print(returned_list[i])


if __name__ == "__main__":

    while True:
        echo_main()
        choice = input(_YOUR_CHOICE)

        if choice == '2':
            echo_syntax()

        seq_input = input(_YOUR_SEQ)
        print("[#]")

        if choice == '1':
            if not utils.is_all_terms_are_fixed_numbers(seq_input):
                print(_NO_PATTERN)
                continue
            ret = eng.unordered_search(seq_input)
            print_ret(ret)

        elif choice == '2':
            if not utils.is_seq_contains_fixed_numbers(seq_input):
                print(_ONE_NUMBER)
                continue
            ret = eng.ordered_search(seq_input)
            print_ret(ret)

        elif choice == '3':
            if not utils.is_all_terms_are_fixed_numbers(seq_input):
                print(_NO_PATTERN)
                continue
            echo_advanced()
            choice = input(_YOUR_CHOICE)
            ############################################################################################################
            if choice == '1':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                eng1.adv_search_shift_constant(seq_input, int(range_param))
                pass

            elif choice == '2':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                eng1.adv_search_scale_constant(seq_input, int(range_param))
                pass

            elif choice == '3':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                eng1.adv_search_shift_n(seq_input, int(range_param))
                pass

            elif choice == '4':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                eng1.adv_search_scale_n(seq_input, int(range_param))
                pass

            elif choice == '5':
                range_param = input(_MAX_SHIFT_VALUE_N_TO_N)
                eng1.adv_search_shift_and_scale_constant(seq_input, int(range_param))
                pass

            elif choice == '6':
                range_param = input(_MAX_N_VALUE_N_TO_N)
                eng1.adv_search_shift_and_scale_n(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '7':
                range_param = input(_MAX_LEVEL_VALUE)
                eng2.adv_search_adjacent_terms_difference(seq_input, int(range_param))
                pass

            elif choice == '8':
                range_param = input(_MAX_LEVEL_VALUE)
                eng2.adv_search_adjacent_terms_sum(seq_input, int(range_param))
                pass

            elif choice == '9':
                range_param = input(_MAX_LEVEL_VALUE)
                eng2.adv_search_adjacent_terms_product(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '10':
                prime_start = input(_PRIME_START_POINT)
                prime_end = input(_PRIME_END_POINT)
                eng3.adv_search_primes_shift(seq_input, int(prime_start), int(prime_end))
                pass

            elif choice == '11':
                prime_start = input(_PRIME_START_POINT)
                prime_end = input(_PRIME_END_POINT)
                eng3.adv_search_primes_scale(seq_input, int(prime_start), int(prime_end))
                pass
            ############################################################################################################
            elif choice == '12':
                shift_tolerance = input(_TOLERANCE_VALUE)
                eng4.adv_search_find_similar(seq_input, int(shift_tolerance))
                pass

            elif choice == '13':
                eng4.adv_search_summation_of_two_seq(seq_input)
                pass

            elif choice == '14':
                eng4.adv_search_product_of_two_seq(seq_input)
                pass
            ############################################################################################################
            elif choice == '15':
                range_param = input(_MAX_LEVEL_VALUE)
                eng2.adv_search_cumulative_sum(seq_input, int(range_param))
                pass

            elif choice == '16':
                range_param = input(_MAX_LEVEL_VALUE)
                eng2.adv_search_cumulative_product(seq_input, int(range_param))
                pass
            ############################################################################################################
            elif choice == '17':
                range_param = input(_MAX_LEVEL_VALUE)
                eng5.adv_search_differences(seq_input, int(range_param))
                pass

            elif choice == '18':
                range_param = input(_MAX_LEVEL_VALUE)
                eng5.adv_search_sums(seq_input, int(range_param))
                pass

            elif choice == '19':
                range_param = input(_MAX_LEVEL_VALUE)
                eng5.adv_search_products(seq_input, int(range_param))
                pass

            elif choice == '20':
                range_param = input(_MAX_LEVEL_VALUE)
                eng5.adv_search_cumulative_sum(seq_input, int(range_param))
                pass

            elif choice == '21':
                range_param = input(_MAX_LEVEL_VALUE)
                eng5.adv_search_cumulative_product(seq_input, int(range_param))
                pass
            ############################################################################################################
