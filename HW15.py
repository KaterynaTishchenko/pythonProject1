def format_time(seconds):
    days, remainder = divmod(seconds, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        days_word = "день"
    elif 2 <= days <= 4:
        days_word = "дні"
    else:
        days_word = "днів"

    formatted_time = "{:d} {}, {:02d}:{:02d}:{:02d}".format(days, days_word, hours, minutes, seconds)
    return formatted_time

seconds = int(input("Введіть кількість секунд: "))

if seconds < 0 or seconds >= 8640000:
    print("Некоректне значення! Введене число повинно бути більше або дорівнювати 0 і менше ніж 8640000.")
else:
    print(format_time(seconds))
