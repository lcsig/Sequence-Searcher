import search_engine.seq as utils
import search_engine.normal_search as eng


"""
Contains: 
1. Shift The Sequence with Constant and Search
2. Scale The Sequence with Constant and Search
3. Shift The Sequence with (N, N+1, N+2 ...) and Search
4. Scale The Sequence with (N, N+1, N+2 ...) and Search
5. Scale and Shift The Sequence with Constant and Search
6. Scale and Shift The Sequence with (N, N+1, N+2 ...) and Search
"""


def adv_search_shift_constant(seq: str, max_constant: int):
    """
    Shift The Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one of them will be added each time to the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_shifted = list(numeric_seq)
    for i in range(-1 * max_constant, max_constant + 1):
        if i == 0:
            continue

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_shifted[n] = numeric_seq[n] + i
        string_seq_shifted = ','.join(str(x) for x in numeric_seq_shifted)

        eng.search_and_echo(string_seq_shifted, i, "Shift Value")


def adv_search_scale_constant(seq: str, max_constant: int):
    """
    Multiply The Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one of them will be multiplied each time to the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_multiplied = list(numeric_seq)
    for i in range(-1 * max_constant, max_constant + 1):
        if i == 0 or i == 1:
            continue

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_multiplied[n] = numeric_seq[n] * i
        string_seq_multiplied = ','.join(str(x) for x in numeric_seq_multiplied)

        eng.search_and_echo(string_seq_multiplied, i, "Multiplication Value")


def adv_search_shift_n(seq: str, max_constant: int):
    """
    Shift The Sequence by Another Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one represents the beginning of individual sequence that will be added to the
        target sequence in the input
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_shifted = list(numeric_seq)
    for i in range(-1 * max_constant, max_constant + 1):

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_shifted[n] = numeric_seq[n] + (i + n)
        string_seq_shifted = ','.join(str(x) for x in numeric_seq_shifted)

        eng.search_and_echo(string_seq_shifted, i, "Shift Value")


def adv_search_scale_n(seq: str, max_constant: int):
    """
    Multiply The Sequence by Another Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one represents the beginning of individual sequence that will be multiplied
        to the target sequence in the input
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_multiplied = list(numeric_seq)
    for i in range(-1 * max_constant, max_constant + 1):

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_multiplied[n] = numeric_seq[n] * (i + n)
        string_seq_multiplied = ','.join(str(x) for x in numeric_seq_multiplied)

        eng.search_and_echo(string_seq_multiplied, i, "Multiplication Value")


def adv_search_shift_and_scale_constant(seq: str, constant: int):
    """
    Shift and Scale The Sequence with Constant and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one represents the beginning of individual constant that will be added to the
        target sequence and multiplied to it
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_shifted = list(numeric_seq)
    for i in range(-1 * constant, constant + 1):
        if i == 0:
            continue

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_shifted[n] = numeric_seq[n] * i + i
        string_seq_shifted = ','.join(str(x) for x in numeric_seq_shifted)

        eng.search_and_echo(string_seq_shifted, i, "Shift Value")


def adv_search_shift_and_scale_n(seq: str, max_constant: int):
    """
    Shift/Scale and Scale/shift with Sequence and Search
    seq: A string that contains a comma seperated numbers
    max_constant: (1 to max_constant) each one represents the beginning of individual sequence that will be added to the
        target sequence in the input
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    numeric_seq_multiplied = list(numeric_seq)
    for i in range(-1 * max_constant, max_constant + 1):
        if i == 0:
            continue

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_multiplied[n] = numeric_seq[n] * i + (n + 1)
        string_seq_multiplied = ','.join(str(x) for x in numeric_seq_multiplied)

        eng.search_and_echo(string_seq_multiplied, i, "Multiplication Value (x * constant + n(i))")

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_multiplied[n] = numeric_seq[n] * (n + 1) + i
        string_seq_multiplied = ','.join(str(x) for x in numeric_seq_multiplied)

        eng.search_and_echo(string_seq_multiplied, i, "Multiplication Value (x * n(i) + constant)")

        # Calculate the Sequence
        for n in range(len(numeric_seq)):
            numeric_seq_multiplied[n] = numeric_seq[n] * (n + i) + (i + n)
        string_seq_multiplied = ','.join(str(x) for x in numeric_seq_multiplied)

        eng.search_and_echo(string_seq_multiplied, i, "Multiplication Value (x * n(i) + n(i))")
