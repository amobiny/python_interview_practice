

def merge(arr, l_idx, r_idx):
    out = []
    m_idx = (l_idx + r_idx) // 2
    list1, list2 = arr[:m_idx], arr[m_idx:]
    l_list1, l_list2 = len(list1), len(list2)
    i, j = 0, 0
    while i < l_list1 and j < l_list2:
        if list1[i] <= list2[j]:
            out.append(list1[i])
            i += 1
        else:
            out.append(list2[j])
            j += 1

    if i < l_list1 and j == l_list2:
        out += list1[i:]
    if i == l_list1 and j < l_list2:
        out += list2[j:]

    return out


def merge_sort(arr, l_idx, r_idx):
    if len(arr) <= 1:
        return arr

    m_idx = (l_idx + r_idx) // 2
    if m_idx > l_idx:
        merge_sort(arr, l_idx, m_idx)
        merge_sort(arr, m_idx, r_idx)
        arr = merge(arr, l_idx, r_idx)
    return arr


my_arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(my_arr, 0, len(my_arr)))







