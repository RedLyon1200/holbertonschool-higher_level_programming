#!/usr/bin/python3
def best_score(a_dictionary):
    best = {}
    score = 0

    if a_dictionary:
        for w in a_dictionary:
            if a_dictionary[w] > score:
                score = a_dictionary[w]
                best = w
        return best
    else:
        return None
