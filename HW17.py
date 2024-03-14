def correct_sentence(text):
    if not text.endswith(('.', '!', '?')):
        text += '.'

    if not text[0].isupper():
        text = text[0].upper() + text[1:]

    return text

input_sentence = input("Введіть речення для перевірки: ")

corrected_sentence = correct_sentence(input_sentence)
print("Виправлене речення:", corrected_sentence)
