# Початковий список
lst = [0, 1, 0, 12, 3]

# Використовуємо дві змінні для відстеження позиції наступного нуля та позиції для обміну ненульового елемента
next_zero_index = 0

# Переміщаємо всі ненульові елементи на початок списку
for i in range(len(lst)):
    if lst[i] != 0:
        lst[next_zero_index], lst[i] = lst[i], lst[next_zero_index]
        next_zero_index += 1

# Виводимо результат
print(lst)