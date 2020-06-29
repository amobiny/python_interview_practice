
###########################################################################
# Brute Force
###########################################################################


def magic_index(arr):
    for i, val in enumerate(arr):
        if i == val:
            return i
    return False


my_array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_index(my_array))


###########################################################################
# Iterative
###########################################################################

def magic_index_2(arr):
    l_idx, r_idx = 0, len(arr)-1
    while l_idx <= r_idx:
        m_idx = (l_idx + r_idx) // 2
        if m_idx == arr[m_idx]:
            return m_idx
        elif m_idx < arr[m_idx]:
            r_idx = m_idx - 1
        elif m_idx > arr[m_idx]:
            l_idx = m_idx + 1
    return 0


my_array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_index_2(my_array))


###########################################################################
# Recursive
###########################################################################

def magic_index_3(arr, l_idx, r_idx):
    if l_idx <= r_idx:
        m_idx = (l_idx + r_idx) // 2
        if m_idx == arr[m_idx]:
            return m_idx
        elif m_idx > arr[m_idx]:
            return magic_index_3(arr, m_idx+1, r_idx)
        elif m_idx < arr[m_idx]:
            return magic_index_3(arr, l_idx, m_idx-1)
    else:
        return -1


my_array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_index_3(my_array, 0, len(my_array)-1))
