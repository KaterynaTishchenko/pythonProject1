import string

def get_letters_between(min_letter, max_letter):
    alphabet = string.ascii_letters
    min_index = alphabet.index(min_letter)
    max_index = alphabet.index(max_letter)
    return alphabet[min_index:max_index + 1]

letters_range = input("Введіть діапазон літер через дефіс: ")

min_letter, max_letter = letters_range.split('-')

print(get_letters_between(min_letter, max_letter))