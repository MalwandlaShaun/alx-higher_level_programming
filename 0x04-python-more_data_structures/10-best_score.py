#!/usr/bin/python3


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        max_score = 0
        highest = ""
        for i in my_list:
            if a_dictionary[i] > max_score:
                max_score = a_dictionary[i]
                highest = i
        return highest
