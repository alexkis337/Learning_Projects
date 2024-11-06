def b_search(array: list, item_to_find: int):
    first = 0
    last = len(array) - 1

    while first < last:
        mid = (first + last) // 2
        if item_to_find == array[mid]:
            return 'item at pos ' + str(mid)
        else:
            if item_to_find < mid:
                last = mid - 1
            else:
                first = mid + 1


print(b_search([1, 3, 6, 8, 9, 20, 34, 2, 22, 6, 8, 7], 8))