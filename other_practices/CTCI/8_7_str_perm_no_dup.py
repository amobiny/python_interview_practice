
def insert_char_at(str_, char_, loc):
    return str_[:loc] + char_ + str_[loc:]


def get_perms(str_):
    permutations = []
    if len(str_) == 0:
        return permutations.append('')

    first_char, remainder = str_[0], str_[1:]
    words = get_perms(remainder)
    for j, word in enumerate(words):
        for loc_ in range(len(remainder)+1):
            permutations.append(insert_char_at(remainder, first_char, loc_))

    return permutations


print(get_perms('abcd'))


