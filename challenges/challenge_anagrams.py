def is_anagram(first_string, second_string):
    if (
        not first_string or not second_string
        or len(first_string) != len(second_string)
    ):
        return False

    first, second = list(first_string.lower()), list(second_string.lower())

    for index in first:
        if index in second:
            second.remove(index)
        else:
            return False
    return True
