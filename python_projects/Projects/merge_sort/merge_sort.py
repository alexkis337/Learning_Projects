def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = [3, 1, 4, 8, 5, 3, 2, 6, 9, 7]
merge_sort(array)
print(array)
