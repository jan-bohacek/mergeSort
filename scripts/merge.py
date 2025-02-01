def merge(array, left, right):
    left_n, right_n = len(left), len(right)
    i,j,k = 0,0,0

    while left_n > i and right_n > j:
        if left[i] > right[j]:
            array[k] = right[j]
            j += 1
        else:
            array[k] = left[i]
            i += 1
        k += 1

    while i < left_n:
        array[k] = left[i]
        i += 1
        k += 1
    while j < right_n:
        array[k] = right[j]
        j += 1
        k += 1