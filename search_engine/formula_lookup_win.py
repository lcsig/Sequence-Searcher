import search_engine.utils as utils

from search_engine import seq_list_numeric
from search_engine import seq_list
from .math_exp_eval_engine import NumericStringParser
"""
This file contains the implementations for formula lookup algorithm
"""


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
    return_dic = {}

    exp_input = parse_expression(exp_input)
    n_index = get_index_of_term_n(exp_input)
    number_of_terms = len(exp_input)
    nsp = NumericStringParser()

    # Iterate over sequences
    for i in range_list:
        seq = list(seq_list_numeric[i])

        # Iterate over terms one by one
        for d in range(len(seq) - number_of_terms):
            seq_cut = seq[d:(d + number_of_terms)]

            if formula_lookup_terms_by_terms(nsp, exp_input, seq_cut, n_index):
                return_dic[seq_list[i]] = d
                break

        utils.waiting(i, len(seq_list_numeric))

    return return_dic


def formula_lookup(exp_input: str):
    """
    This method will search about sequences using terms lookup formula (n -10, n, n * 10, n * 20)
    exp_input: The terms lookup formula.
    returns: A dictionary where the key represents the sequence and the value represents terms index where the
        formula has matched.
    """
    if not is_expression_correct(exp_input):
        raise ValueError("The expression syntax is wrong!")

    # Divide Range
    number_of_sequences = len(seq_list_numeric)
    return_dic = formula_lookup_linear_search(exp_input, range(number_of_sequences))

    # Return
    return return_dic