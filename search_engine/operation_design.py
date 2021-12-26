import search_engine.utils as utils
from search_engine import seq_list_numeric
from search_engine import seq_list


def operation_design(transform_on_oeis, transform_on_input, filter_function, input_seq: str):
    """
    A function that represents some kind of framework to make operations and transformations on sequences.
    oeis_transform: A function which will be applied on the OEIS sequences.
    input_transform: A function which will be applied on the input sequence.
    filter_fun: A function that will receive the OEIS and the input sequence and return False/True to filter the results
    seq: A string that contains a comma seperated numbers.
    returns: A list of the sequences that have matched.
    """
    input_seq_transformed = utils.convert_str_to_list(input_seq, True, False)
    input_seq_transformed = transform_on_input(input_seq_transformed)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        oeis_sequence = transform_on_oeis(list(seq_list_numeric[i]))

        if filter_function(list(oeis_sequence), list(input_seq_transformed)):
            result_list.append(seq_list[i])

        utils.waiting(i, len(seq_list_numeric))

    return result_list

