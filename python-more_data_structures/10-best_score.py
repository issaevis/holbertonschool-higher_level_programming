def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maximum = 0
    best_key = None
    for key in a_dictionary:
        if a_dictionary[key] > maximum:
            maximum = a_dictionary[key]
            best_key = key
    return best_key
