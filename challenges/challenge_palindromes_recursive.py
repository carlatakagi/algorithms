def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if high_index == 0:
        return True
    else:
        if word[low_index].upper() != word[high_index].upper():
            return False
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
