import re
import search_engine.utils as utils
from search_engine import convert_str_to_list
from search_engine import seq_list_numeric
from search_engine import seq_list


def parse_pattern(seq: str):
    """
    A function to substitute RegEx in the sequence string
    sequence: A string that contains a comma seperated numbers and patterns
    returns: A string after replacing the patterns with a specific regex
    """
    _RE1 = r'(\+|-)?\d+'
    _RE2 = '.+'

    # Clear seq from spaces
    seq = seq.replace(" ", "")

    # Replace with Regex
    terms = seq.split(",")
    for idx in range(0, len(terms)):
        if ":" in terms[idx]:
            terms[idx] = _RE1
        elif "?*" in terms[idx]:
            terms[idx] = _RE2
        elif "?" in terms[idx] and not ("?*" in terms[idx]):
            num_terms = int(terms[idx].replace("?", ""))
            terms[idx] = ""
            for d in range(0, num_terms):
                terms[idx] = terms[idx] + _RE1 + ","
            terms[idx] = terms[idx][0:-1]  # remove ',' from the last term

    seq_returned = ""
    for idx in range(0, len(terms)):
        seq_returned += terms[idx] + ","
    seq_returned = seq_returned[0:-1]
    return seq_returned


def unordered_search(numbers_set: str, max_off_terms: int):
    """
    Search about set of numbers in OEIS sequences without considering the input numbers order
    numbers_set: The sequence or set of numbers that will be searched about
    max_off_terms: The number of terms allowed to be dropped
    returns: A dictionary where the value represents the rank of match, and the dictionary value represents the sequence
    """
    seq = convert_str_to_list(numbers_set, True, False)
    return_dic = {}

    for i in range(len(seq_list_numeric)):
        exist_in_oeis = True
        dropped_terms = max_off_terms

        for n in range(len(seq)):
            if seq[n] not in seq_list_numeric[i]:
                dropped_terms -= 1
            if dropped_terms < 0:
                exist_in_oeis = False
                break
        if exist_in_oeis:
            return_dic.setdefault(dropped_terms, []).append(seq_list[i])

    return return_dic


def is_seq_valid(seq_pattern: str, probable_seq: str):
    """
    seq_pattern: The input from the user (E.g., 1,2,?1,10,15--30)
    probable_seq: A sequence of integers to check if the sequence is applied for the pattern
    return: True if the probable sequence is fit on the pattern input
    """
    x = seq_pattern.split(",")
    y = probable_seq.split(",")
    idx = 0
    for i in range(len(x)):
        if x[i].strip().strip("+-").isdigit():
            if x[i].strip() == y[idx].strip():
                idx += 1
                continue
            else:
                return False

        elif ":" in x[i]:
            k = x[i].strip().split(":")
            first_num = int(k[0])
            second_num = int(k[1])
            val = int(y[idx])
            if not (first_num <= val <= second_num):
                return False

            idx += 1
        elif "?*" in x[i]:
            next_term = x[i + 1]
            validate_next_term = -1
            for n in range(idx, len(y)):
                if is_seq_valid(next_term, y[n]):
                    validate_next_term = n
                    break

            if validate_next_term == -1:
                return False
            else:
                idx = validate_next_term

        elif "?" in x[i]:
            idx += int(x[i].strip().strip("?"))
            pass

    return True


def ordered_search(seq: str):
    """
    Search about a sequence - Support Patterns Search
    returns: A list of sequences that contains all the matching sequence
    """
    seq_returned: list
    seq = seq.replace(" ", "")

    if not utils.is_pattern_exist(seq):
        seq_returned = sequence_search_no_pattern(seq)

    else:
        # Parse Sequence
        seq_parsed = parse_pattern(seq)

        # Dictionary For Regex
        re_data = {}

        # Apply Regex and Save The Findings
        for i in range(0, len(seq_list)):
            seq_re_applied = re.finditer(seq_parsed, seq_list[i])
            groups = []
            for n in seq_re_applied:
                groups.append(n.group(0))
            if len(groups) >= 1:
                re_data[seq_list[i]] = groups

        # Filter
        seq_keys = list(re_data.keys())
        for i in range(0, len(seq_keys)):
            seq_vals = re_data[seq_keys[i]]

            for n in range(len(seq_vals) - 1, -1, -1):
                seq_for_check = seq_vals[n]
                if not is_seq_valid(seq, seq_for_check):
                    del seq_vals[n]

            if len(seq_vals) == 0:
                re_data.pop(seq_keys[i])

        seq_returned = list(re_data.keys())

    return seq_returned


def sequence_search_no_pattern(seq: str):
    """
    A function to search about a sequence that has no patterns in the sequences DB
    """
    seq_returned = []
    seq = seq.replace(" ", "")

    for i in range(0, len(seq_list)):
        if seq in seq_list[i]:
            seq_returned.append(seq_list[i])

    return seq_returned


def search_and_echo(sequence_after_applying_operation: str, current_value: int = 0, echo_string: str = ""):
    """
    A function that is used by the advanced search operations
    returns: nothing
    """
    # Search
    returned_list = ordered_search(sequence_after_applying_operation)

    # Echo Sequence
    if echo_string != "":
        print("[+] Current " + echo_string + ": " + str(current_value))

    # Echo Results
    print("    Current Seq ---> " + sequence_after_applying_operation)
    if len(returned_list) == 0:
        print("    Results ---> Nothing Found", end='')
    else:
        print("    Results ---> ", end='')
        for d in range(0, len(returned_list)):
            print(returned_list[d][0:returned_list[d].find(',')], end='')

    # Done
    print("\n[#]")
