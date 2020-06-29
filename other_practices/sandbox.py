

def is_palindrome(input_str):
    is_odd = set()
    for char_ in input_str:
        if char_ in is_odd:
            is_odd.discard(char_)
        else:
            is_odd.add(char_)

    return True if len(is_odd) <= 1 else False


a = 'a'
print(a.isalpha())

# print(is_palindrome('civic'))

