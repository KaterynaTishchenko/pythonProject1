def move_zeroes_to_end(lst):
    # Використовуємо дві змінні для відстеження позиції наступного нуля та позиції для обміну ненульового елемента
    next_zero_index = 0

    # Переміщаємо всі ненульові елементи на початок списку
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[next_zero_index], lst[i] = lst[i], lst[next_zero_index]
            next_zero_index += 1

    return lst


# Приклади для перевірки
print(move_zeroes_to_end([0, 1, 0, 12, 3]))  # [1, 12, 3, 0, 0]
print(move_zeroes_to_end([0]))  # [0]
print(move_zeroes_to_end([1, 0, 13, 0, 0, 0, 5]))  # [1, 13, 5, 0, 0, 0, 0]
print(move_zeroes_to_end(
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))  # [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
