import modules.seq as utils
import modules.seq_calc as utils_calc


"""
Contains:
12. Search About Similar Sequence
13. Check if the Sequence is The Summation of Two Sequences
14. Check if The Sequence is The Product of Two Sequences
"""

seq_list = utils.seq_list
seq_list_numeric = utils.seq_list_numeric


def adv_search_find_similar(seq: str, tolerance_value: int):
    """
    Search About Similar Sequence by Setting a Tolerance Value on Each Term in The Sequence
    seq: A string that contains a comma seperated numbers
    tolerance_value: A tolerance value where each term could be -+tolerance_value
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        if utils.list_a_in_b_similar(numeric_seq, seq_list_numeric[i], tolerance_value):
            result_list.append(i + 1)

        utils.waiting(i, len(seq_list_numeric))

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print("A" + str(result_list[i]))


def adv_search_summation_of_two_seq(seq: str):
    """
    Check If the Sequence is The Summation of Two Sequences
    seq: A string that contains a comma seperated numbers
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        for n in range(i + 1, len(seq_list_numeric)):
            seq_result = utils_calc.add_sequences(seq_list_numeric[i], seq_list_numeric[n])
            if utils.list_a_in_b(numeric_seq, seq_result):
                result_list.append([i + 1, n + 1])

        # Progress ...
        utils.waiting(i, len(seq_list_numeric))

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print("A" + str(result_list[i][0]) + " <--> " + "A" + str(result_list[i][1]))


def adv_search_product_of_two_seq(seq: str):
    """
    Check If the Sequence is The Product of Two Sequences
    seq: A string that contains a comma seperated numbers
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        for n in range(i + 1, len(seq_list_numeric)):
            seq_result = utils_calc.multiply_sequences(seq_list_numeric[i], seq_list_numeric[n])
            if utils.list_a_in_b(numeric_seq, seq_result):
                result_list.append([i + 1, n + 1])

        # Progress ...
        utils.waiting(i, len(seq_list_numeric))

    if len(result_list) == 0:
        print("\n[#] Nothing Found")
    else:
        print("\n[#]")
    for i in range(len(result_list)):
        print("A" + str(result_list[i][0]) + " <--> " + "A" + str(result_list[i][1]))
