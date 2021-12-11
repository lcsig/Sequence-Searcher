import search_engine.seq as utils
import search_engine.seq_calc as utils_calc
import search_engine.normal_search as eng

"""
Contains:
7. Search About Differences of Adjacent Terms
8. Search About Summation of Adjacent Terms
9. Search About Product of Adjacent Terms
15. Search About Cumulative Sums
16. Search About Cumulative Products
"""


def adv_search_adjacent_terms_difference(seq: str, diff_level: int):
    """
    Sequence Differentiation and Search
    seq: A string that contains a comma seperated numbers
    diff_level: The differentiation range (1 to diff_level) that will be applied to the sequence before doing a search
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    if len(numeric_seq) - diff_level < 4:
        print("[!] Choose a higher level")
        return

    diffs_list = utils_calc.seq_adjacent_terms_diff(numeric_seq, diff_level)
    for i in range(diff_level):
        numeric_seq_diff = diffs_list[i]
        string_seq_differentiated = ','.join(str(x) for x in numeric_seq_diff)
        eng.search_and_echo(string_seq_differentiated, i + 1, "Difference Level")


def adv_search_adjacent_terms_sum(seq: str, cum_sum_level: int):
    """
    Search About Cumulative Sums of Sequence
    seq: A string that contains a comma seperated numbers
    cum_sum_level: The cumulative sums range (1 to cum_sum_level) that will be applied to the sequence before searching
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    if len(numeric_seq) - cum_sum_level < 4:
        print("[!] Choose a higher level")
        return

    sums_list = utils_calc.seq_adjacent_terms_sum(numeric_seq, cum_sum_level)
    for i in range(cum_sum_level):
        numeric_seq_cumulative = sums_list[i]
        string_seq_cumulative = ','.join(str(x) for x in numeric_seq_cumulative)
        eng.search_and_echo(string_seq_cumulative, i + 1, "Sum Level")


def adv_search_adjacent_terms_product(seq: str, cum_prod_level: int):
    """
    Search About Cumulative Products of Sequence
    seq: A string that contains a comma seperated numbers
    cum_prod_level: The cumulative products range (1 to cum_sum_level) that will be applied to the sequence
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)
    if len(numeric_seq) - cum_prod_level < 4:
        print("[!] Choose a higher level")
        return

    products_list = utils_calc.seq_adjacent_terms_prod(numeric_seq, cum_prod_level)
    for i in range(cum_prod_level):
        numeric_seq_cum_product = products_list[i]
        string_seq_cum_product = ','.join(str(x) for x in numeric_seq_cum_product)
        eng.search_and_echo(string_seq_cum_product, i + 1, "Product Level")


def adv_search_cumulative_sum(seq: str, cum_sum_level: int):
    """
    Search About Cumulative Sums of Sequence
    seq: A string that contains a comma seperated numbers
    cum_sum_level: The cumulative sums range (1 to cum_sum_level) of levels
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    cum_sum_list = utils_calc.seq_cumulative_sum(numeric_seq, cum_sum_level)
    for i in range(cum_sum_level):
        numeric_seq_cumulative = cum_sum_list[i]
        string_seq_cumulative = ','.join(str(x) for x in numeric_seq_cumulative)
        eng.search_and_echo(string_seq_cumulative, i + 1, "Cumulative Sum Level")


def adv_search_cumulative_product(seq: str, cum_prod_level: int):
    """
    Search About Cumulative Products of Sequence
    seq: A string that contains a comma seperated numbers
    cum_prod_level: The cumulative product range (1 to cum_prod_level) of levels
    returns: nothing
    """
    numeric_seq = utils.convert_str_to_list(seq, True, False)

    cum_product_list = utils_calc.seq_cumulative_product(numeric_seq, cum_prod_level)
    for i in range(cum_prod_level):
        numeric_seq_cum_product = cum_product_list[i]
        string_seq_cum_product = ','.join(str(x) for x in numeric_seq_cum_product)
        eng.search_and_echo(string_seq_cum_product, i + 1, "Cumulative Product Level")
