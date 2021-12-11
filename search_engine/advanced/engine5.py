import search_engine.seq as utils
import search_engine.seq_calc as utils_calc

"""
Contains:
17. Check if The Input is a Difference of A Sequence in The Database
18. Check if The Input is a Sum of Adjacent Terms of A Sequence in The Database
19. Check if The Input is a Product of Adjacent Terms of A Sequence in The Database
20. Check if The Input is a Cumulative Sum of A Sequence in The Database
21. Check if The Input is a Cumulative Product of A Sequence in The Database
"""

from search_engine import seq_list_numeric


def print_result_list(result_list):
    print("[#]")
    print("[+] Results: ")
    if len(result_list) == 0:
        print("[!] Nothing Found")
        return

    for i in range(len(result_list)):
        print("A" + str(result_list[i][0]) + " <--> " + "Operation Level: " + str(result_list[i][1]))


def adv_search_differences(seq: str, max_diff_level: int):
    """
    Check If the Sequence is The Result of the Adjacent Terms Difference Operation on Sequence in The Database
    seq: A string that contains a comma seperated numbers
    max_diff_level: The maximum number of adjacent differences operations that will be performed on the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        seq_result = utils_calc.seq_adjacent_terms_diff(seq_list_numeric[i], max_diff_level)

        for diff_level in range(max_diff_level):
            if utils.list_a_in_b(numeric_seq, seq_result[diff_level]):
                result_list.append([i + 1, diff_level + 1])

        utils.waiting(i, len(seq_list_numeric))

    print_result_list(result_list)


def adv_search_sums(seq: str, max_sum_level: int):
    """
    Check If the Sequence is The Result of the Adjacent Terms Sum Operation on Sequence in The Database
    seq: A string that contains a comma seperated numbers
    max_sum_level: The maximum number of adjacent summation operations that will be performed on the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        seq_result = utils_calc.seq_adjacent_terms_sum(seq_list_numeric[i], max_sum_level)

        for sum_level in range(max_sum_level):
            if utils.list_a_in_b(numeric_seq, seq_result[sum_level]):
                result_list.append([i + 1, sum_level + 1])

        utils.waiting(i, len(seq_list_numeric))

    print_result_list(result_list)


def adv_search_products(seq: str, max_product_level: int):
    """
    Check If the Sequence is The Result of the Adjacent Terms Product Operation on Sequence in The Database
    seq: A string that contains a comma seperated numbers
    max_product_level: The maximum number of adjacent products operations that will be performed on the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        seq_result = utils_calc.seq_adjacent_terms_prod(seq_list_numeric[i], max_product_level)

        for prod_level in range(max_product_level):
            if utils.list_a_in_b(numeric_seq, seq_result[prod_level]):
                result_list.append([i + 1, prod_level + 1])

        utils.waiting(i, len(seq_list_numeric))

    print_result_list(result_list)


def adv_search_cumulative_sum(seq: str, max_cumsum_level: int):
    """
    Check If the Sequence is The Result of the Cumulative Sum Operation on Sequence in The Database
    seq: A string that contains a comma seperated numbers
    max_cumsum_level: The maximum number of cumulative sum operations that will be performed on the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        seq_result = utils_calc.seq_cumulative_sum(seq_list_numeric[i], max_cumsum_level)

        for sum_level in range(max_cumsum_level):
            if utils.list_a_in_b(numeric_seq, seq_result[sum_level]):
                result_list.append([i + 1, sum_level + 1])

        utils.waiting(i, len(seq_list_numeric))

    print_result_list(result_list)


def adv_search_cumulative_product(seq: str, maximum_prod_level):
    """
    Check If the Sequence is The Result of the Cumulative Product Operation on Sequence in The Database
    seq: A string that contains a comma seperated numbers
    maximum_prod_level: The maximum number of cumulative product operations that will be performed on the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    result_list = []
    for i in range(0, len(seq_list_numeric)):
        seq_result = utils_calc.seq_cumulative_product(seq_list_numeric[i], maximum_prod_level)

        for prod_level in range(maximum_prod_level):
            if utils.list_a_in_b(numeric_seq, seq_result[prod_level]):
                result_list.append([i + 1, prod_level + 1])

        utils.waiting(i, len(seq_list_numeric))

    print_result_list(result_list)
