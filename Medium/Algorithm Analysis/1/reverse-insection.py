def insertion_sort_descending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] < key:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = key

    return lst

print(insertion_sort_descending([1, 34,  28, 224, 42, 42, 4]))