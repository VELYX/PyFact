def sum_nested_list(lst):
    total_so_far = 0

    for item in lst:
        if isinstance(item, int):
            total_so_far += item
        elif isinstance(item, list):
            total_so_far += sum_nested_list(item)
    return total_so_far
