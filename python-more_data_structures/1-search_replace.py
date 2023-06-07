def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = my_list.copy()
        count = new_list.count(search)
        for i in range(count):
            idx = new_list.index(search)
            new_list[idx] = replace
        return new_list
    return None
