import modules.seq as utils
import modules.seq_calc as utils_calc

"""
Contains:
10. Shift with Primes and Search
11. Scale with Primes and Search
"""

seq_list = utils.seq_list
seq_list_numeric = utils.seq_list_numeric


def adv_search_primes_shift(seq: str, prime_start_point: int, prime_end_point: int):
    """
    Add Primes to The Sequence and Search
    seq: A string that contains a comma seperated numbers
    prime_start_point: The starting point of the primes sequence
    prime_start_point: The ending point of the primes sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    primes_list = utils.generate_primes(prime_start_point, prime_end_point)

    if len(primes_list) < len(numeric_seq):
        print("[!] Choose A Bigger Range")
        return

    for i in range(len(primes_list) - len(numeric_seq) + 1):

        # Calculate the Sequence
        numeric_seq_primes_added = utils_calc.add_sequences(numeric_seq, primes_list[i:(len(numeric_seq) + i)])
        string_seq_primes_added = ','.join(str(x) for x in numeric_seq_primes_added)

        utils.search_and_echo(string_seq_primes_added, primes_list[i], "Primes Start Point")


def adv_search_primes_scale(seq: str, prime_start_point: int, prime_end_point: int):
    """
    Multiply The Sequence with Primes and Search
    seq: A string that contains a comma seperated numbers
    prime_start_point: The starting point of the primes sequence
    prime_start_point: The ending point of the primes sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    primes_list = utils.generate_primes(prime_start_point, prime_end_point)

    if len(primes_list) < len(numeric_seq):
        print("[!] Choose A Bigger Range")
        return

    for i in range(len(primes_list) - len(numeric_seq) + 1):

        # Calculate the Sequence
        numeric_seq_primes_added = utils_calc.multiply_sequences(numeric_seq, primes_list[i:(len(numeric_seq) + i)])
        string_seq_primes_added = ','.join(str(x) for x in numeric_seq_primes_added)

        utils.search_and_echo(string_seq_primes_added, primes_list[i], "Primes Start Point")
