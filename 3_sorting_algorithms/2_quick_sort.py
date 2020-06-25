# partitions an array around a pivot element (pick the last element as pivot)
# partitioning can be done in linear time ( O(n) )
# Then (recursively) sort the elements that lies on the left and right of the pivot


def partition(arr, l_idx, r_idx):
    pivot = arr[r_idx]
    i = l_idx                  # important init (counter of the numbers smaller than the pivot = final index of pivot)
    for j in range(l_idx, r_idx):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r_idx] = arr[r_idx], arr[i]
    return i                                    # ###############


def quick_sort(arr, l_idx, r_idx):
    if l_idx < r_idx:
        pivot_idx = partition(arr, l_idx, r_idx)
        quick_sort(arr, l_idx, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, r_idx)
    return arr


test_list = [3, 8, 2, 5, 1, 4, 7, 6]
print(quick_sort(test_list, 0, len(test_list)-1))


# time_complexity: O(n * log(n)) on average
# requires minimal extra memory
# space_complexity: O(1)
