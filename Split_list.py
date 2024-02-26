def split_list(lst):
    if not lst:
        return [[], []]

    if len(lst) % 2 == 0:
        middle = len(lst) // 2
    else:
        middle = len(lst) // 2 + 1

    first_half = lst[:middle]
    second_half = lst[middle:]

    return [first_half, second_half]


print(split_list([1, 2, 3, 4, 5, 6]))  # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))  # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))  # [[1, 2, 3], [4, 5]]
print(split_list([1]))  # [[1], []]
print(split_list([]))  # [[], []]