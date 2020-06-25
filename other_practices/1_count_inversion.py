# count the number of inversions in a list of elements
# inversion: if i > j and A[i] < A[j]
# example: the answer is zero for a sorted array


def merge_sort_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a, ai = merge_sort_inversions(a)
        b, bi = merge_sort_inversions(b)
        c = []
        i = 0
        j = 0
        inversion_count = ai + bi
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                inversion_count += len(a) - i
                c.append(b[j])
                j += 1
        c += a[i:]
        c += b[j:]
    return c, inversion_count


test_list = [1, 3, 5, 2, 4, 6]
sorted_list, count = merge_sort_inversions(test_list)
print()



