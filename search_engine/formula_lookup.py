import time

import search_engine.seq as utils
import multiprocessing

from search_engine import seq_list_numeric
from search_engine import seq_list
from .math_exp_eval_engine import NumericStringParser

"""
This file contains the implementations for formula lookup algorithm
"""
return_dic: dict
progress: multiprocessing.Value
lock: multiprocessing.Manager().Lock
_NUMBER_OF_THREADS = 8


def is_expression_correct(exp_input: str):
    """
    A function to validate the syntax of the input that represents the terms formula lookup
    exp_input: The terms lookup formula.
    returns: True if the syntax is valid, False otherwise.
    """
    try:
        nsp = NumericStringParser()

        # Parse terms and trim spaces
        exp_input = exp_input.lower().split(',')
        exp_input = list(map(lambda term_of_sequence: str(term_of_sequence).strip(), exp_input))

        # Calculate and Compare
        for i in range(len(exp_input)):
            term = exp_input[i].replace('n', '1000')
            x = nsp.eval(term)

        return True
    except:
        return False


def formula_lookup_terms_by_terms(nsp: NumericStringParser, exp_input: list, sequence: list, n_index: int):
    """
    This method will search about sequences using terms lookup formula (n -10, n, n * 10, n * 20)
    nsp: Instance of NumericStringParser
    exp_input: The terms lookup formula.
    sequence: A sequence that must have the same length of terms as the terms lookup formula
    n_index: The index of the term the represents n
    returns: True if matched, False otherwise.
    """
    n = sequence[n_index]

    # Calculate and Compare
    for i in range(len(exp_input)):
        term = exp_input[i].replace('n', str(n))
        if nsp.eval(term) != sequence[i]:
            return False

    return True


def parse_expression(exp_input: str):
    exp_input = exp_input.lower().split(',')
    exp_input = list(map(lambda x: str(x).strip(), exp_input))
    return exp_input


def get_index_of_term_n(exp_input: list):
    for i in range(len(exp_input)):
        if exp_input[i] == 'n':
            return i


def formula_lookup_linear_search(exp_input: str, range_list):
    """
    This method will search about sequences using terms lookup formula (n -10, n, n * 10, n * 20)
    exp_input: The terms lookup formula.
    start_index: The start index of seq_list_numeric to begin the search with it. Included ---> [start_index, end_index)
    end_index: The end index of seq_list_numeric to end the search with it. Not included ---> [start_index, end_index)
    returns: A dictionary where the key represents the sequence and the value represents terms index where the
        formula has matched.
    """
    # Parse terms and trim spaces
    global progress
    global return_dic
    global lock
    if not ('lock' in vars() or 'lock' in globals()):
        # Make it works without a direct call from formula_lookup
        lock = multiprocessing.Manager().Lock()
        progress = multiprocessing.Value('i', 0)
        return_dic = multiprocessing.Manager().dict()

    exp_input = parse_expression(exp_input)
    n_index = get_index_of_term_n(exp_input)
    number_of_terms = len(exp_input)
    nsp = NumericStringParser()

    # Iterate over sequences
    for i in range_list:
        seq = seq_list_numeric[i]
        with lock:
            progress.value += 1

        # Iterate over terms one by one
        for d in range(len(seq) - number_of_terms):
            seq_cut = seq[d:(d + number_of_terms)]

            if formula_lookup_terms_by_terms(nsp, exp_input, seq_cut, n_index):
                return_dic[seq_list[i]] = d
                break

    return return_dic


def range_split(range_to_split, number_of_groups):
    k, m = divmod(len(range_to_split), number_of_groups)
    return (range_to_split[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(number_of_groups))


def formula_lookup(exp_input: str):
    """
    This method will search about sequences using terms lookup formula (n -10, n, n * 10, n * 20)
    exp_input: The terms lookup formula.
    returns: A dictionary where the key represents the sequence and the value represents terms index where the
        formula has matched.
    """
    global return_dic
    global progress
    global lock
    lock = multiprocessing.Manager().Lock()
    progress = multiprocessing.Value('i', 0)
    return_dic = multiprocessing.Manager().dict()

    if not is_expression_correct(exp_input):
        raise ValueError("The expression syntax is wrong!")

    # Divide Range
    process_list = []
    number_of_sequences = len(seq_list_numeric)
    indices_range = list(range_split(range(number_of_sequences), _NUMBER_OF_THREADS))

    # Start Processes
    for i in range(_NUMBER_OF_THREADS):
        proc = multiprocessing.Process(target=formula_lookup_linear_search, args=(exp_input, indices_range[i]))
        proc.start()
        process_list.append(proc)

    # Wait and Echo
    index = 0
    while progress.value != number_of_sequences:
        utils.waiting_with_index(index, progress.value, number_of_sequences)
        index += 1
        time.sleep(0.25)
    print("")

    # Join
    for process in process_list:
        process.join()

    # Return
    return return_dic
