

def echo_main():
    print("[+] 1. Search about set of numbers in a sequence.")
    print("[+] 2. Search about a sequence.")
    print("[+] 3. Fuzzy Matching.")
    print("[+] 4. Search by Terms Lookup Formula.")
    print("[+] 5. Advanced Search")
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


def get_sequence_name(sequence: str):
    return sequence[0:sequence.find(',')].strip()


def print_ret(returned_list: list):
    if len(returned_list) == 0:
        print("[!] Could not find any results!")
    else:
        for i in range(0, len(returned_list)):
            print(get_sequence_name(returned_list[i]))
            # print(returned_list[i])


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
