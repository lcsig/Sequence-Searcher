
def maximum_number_of_digits():
    # Definitions
    seq_list: list

    # Loading Strings
    with open("data/stripped") as f:
        seq_list = f.readlines()
    del seq_list[0:4]

    n = 0
    last_seq = 0

    for i in range(len(seq_list)):
        terms = seq_list[i].split(',')

        for d in range(len(terms)):
            term_len = len(terms[d].strip().strip("+-"))
            if term_len > n:
                n = term_len
                last_seq = i + 1

    print(n)
    print(last_seq)


def maximum_number_of_digits_statistics():
    # Definitions
    seq_list: list

    # Loading Strings
    with open("data/stripped") as f:
        seq_list = f.readlines()
    del seq_list[0:4]

    n = 0
    k = [0] * 300

    for i in range(len(seq_list)):
        terms = seq_list[i].split(',')

        n = 0
        for d in range(len(terms)):
            term_len = len(terms[d].strip().strip("+-"))
            if term_len > n:
                n = term_len

        k[n] = k[n] + 1

    for i in range(len(k)):
        print(str(i) + " ----> " + str(k[i]))


maximum_number_of_digits_statistics()