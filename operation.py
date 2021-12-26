

def oeis_transform(seq: list):
    """
    This function will receive an OEIS sequence, you should return the sequence after applying your transformation
    """
    for i in range(len(seq)):
        seq[i] = seq[i] + 1
    return seq


def input_transform(seq: list):
    """
    This function will receive the input sequence, you should return the sequence after applying your transformation
    """
    return seq


def list_a_in_b(a: list, b: list):
    """
    Check if list A elements are exist in list B elements while preserving the order
    returns: True if A in B, False otherwise.
    """
    if len(a) > len(b):
        return False
    elif len(a) == len(b):
        return a == b
    else:
        for seq_start in range(len(b) - len(a) + 1):
            contains_flag = True
            for n in range(len(a)):
                if a[n] != b[seq_start + n]:
                    contains_flag = False
                    break
            if contains_flag:
                return True

        return False


def filter_fun(oeis_sequence_transformed: list, input_sequence_transformed: list):
    """
    This function will filter the sequences based on a specific criteria
    Return True if the sequence match, False otherwise.
    """
    return list_a_in_b(input_sequence_transformed, oeis_sequence_transformed)
