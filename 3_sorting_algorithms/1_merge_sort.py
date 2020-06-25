# https://www.geeksforgeeks.org/merge-sort/
# Merge sort is a Divide and Conquer algorithm


def merge(l_list, r_list):

    out = []
    while len(l_list) != 0 and len(r_list) != 0:
        if l_list[0] >= r_list[0]:
            out.append(r_list[0])
            r_list.remove(r_list[0])
        else:
            out.append(l_list[0])
            l_list.remove(l_list[0])

    if len(l_list) == 0:
        out += r_list
    elif len(r_list) == 0:
        out += l_list

    return out


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l_half = merge_sort(arr[:mid])
    r_half = merge_sort(arr[mid:])
    arr = merge(l_half, r_half)
    return arr


my_arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(my_arr))
