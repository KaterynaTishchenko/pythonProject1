lst = [0, 1, 7, 2, 4, 8]

if not lst:
    result = 0
else:
    sum_even_indices = sum(lst[i] for i in range(0, len(lst), 2))

    last_element = lst[-1]

    result = sum_even_indices * last_element

print(result)