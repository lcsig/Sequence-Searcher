"""
This code contains a set of functions that are used to perform a set of operations on sequences
"""


def seq_adjacent_terms_diff(sequence: list, diff_level: int):
    """
    A function to extract the difference of adjacent terms
    sequence: A list of integers that contains the sequence
    diff_level: The level indicates the number of times the operation will be applied on the sequence
    return: A list of list of integers that contains the sequence after extracting the differences
    """
    seq = sequence
    list_ret = [[0]] * diff_level

    for idx in range(0, diff_level):
        diff_seq = [0] * (len(seq) - 1)
        for n in range(1, len(seq)):
            diff_seq[n - 1] = seq[n] - seq[n - 1]

        list_ret[idx] = diff_seq
        seq = diff_seq

    return list_ret


def seq_adjacent_terms_sum(sequence: list, sum_level: int):
    """
    A function to extract the sums of adjacent terms
    sequence: A list of integers that contains the sequence
    sum_level: The level indicates the number of times the operation will be applied on the sequence
    return: A list of list of integers that contains the sequence after extracting the sums
    """
    seq = sequence
    list_ret = [[0]] * sum_level

    for idx in range(0, sum_level):
        sum_seq = [0] * (len(seq) - 1)
        for n in range(1, len(seq)):
            sum_seq[n - 1] = seq[n] + seq[n - 1]

        list_ret[idx] = sum_seq
        seq = sum_seq

    return list_ret


def seq_adjacent_terms_prod(sequence: list, product_level: int):
    """
    A function to extract the products of adjacent terms
    sequence: A list of integers that contains the sequence
    product_level: The level indicates the number of times the operation will be applied on the sequence
    return: A list of list of integers that contains the sequence after extracting the products
    """
    seq = sequence
    list_ret = [[0]] * product_level

    for idx in range(0, product_level):
        prod_seq = [0] * (len(seq) - 1)
        for n in range(1, len(seq)):
            prod_seq[n - 1] = seq[n] * seq[n - 1]

        list_ret[idx] = prod_seq
        seq = prod_seq

    return list_ret


def seq_cumulative_sum(sequence: list, cumulative_sum_level: int):
    """
    A function to return the cumulative product
    sequence: a list of integers that contains the sequence
    cumulative_sum_level: An integer that indicates the cumulative product level
    return: A list of list of integers that contains the sequence after applying cumulative sum operation
    """
    seq = sequence
    list_ret = [[0]] * cumulative_sum_level

    for idx in range(cumulative_sum_level):
        sum_seq = [0] * (len(seq))
        sum_seq[0] = seq[0]
        for n in range(1, len(seq)):
            sum_seq[n] = sum_seq[n - 1] + seq[n]

        list_ret[idx] = sum_seq
        seq = sum_seq

    return list_ret


def seq_cumulative_product(sequence: list, cumulative_product_level: int):
    """
    sequence: a list of integers that contains the sequence
    cumulative_product_level: An integer that contains the level of required cumulative product
    return: A list of list of integers that contains the sequence after applying cumulative product
    """
    seq = sequence
    list_ret = [[0]] * cumulative_product_level

    for idx in range(cumulative_product_level):
        prod_seq = [0] * (len(seq))
        prod_seq[0] = seq[0]
        for n in range(1, len(seq)):
            prod_seq[n] = prod_seq[n - 1] * seq[n]

        list_ret[idx] = prod_seq
        seq = prod_seq

    return list_ret


def add_sequences(seq1: list, seq2: list):
    """
    A function to add two sequences and return the result
    seq1: A list of integers
    seq2: A list of integers
    returns: seq1 + seq2 as a list
    """
    if len(seq1) == len(seq2):
        return [x + y for x, y in zip(seq1, seq2)]
    elif len(seq1) == 0 or len(seq2) == 0:
        return []
    else:
        smaller_length = len(seq1) if len(seq1) < len(seq2) else len(seq2)
        seq1 = seq1[0:smaller_length]
        seq2 = seq2[0:smaller_length]
        return [x + y for x, y in zip(seq1, seq2)]


def multiply_sequences(seq1: list, seq2: list):
    """
    A function to multiply two sequences and return the result
    seq1: A list of integers
    seq2: A list of integers
    returns: seq1 * seq2 as a list
    """
    if len(seq1) == len(seq2):
        return [x * y for x, y in zip(seq1, seq2)]
    elif len(seq1) == 0 or len(seq2) == 0:
        return []
    else:
        smaller_length = len(seq1) if len(seq1) < len(seq2) else len(seq2)
        seq1 = seq1[0:smaller_length]
        seq2 = seq2[0:smaller_length]
        return [x * y for x, y in zip(seq1, seq2)]
