def correct_sentence(text):
    if not text.endswith(('.', '!', '?')):
        text += '.'

    corrected_text = text.capitalize()

    return corrected_text

input_sentence = input("Введіть речення для перевірки: ")

corrected_sentence = correct_sentence(input_sentence)
print("Виправлене речення:", corrected_sentence)
