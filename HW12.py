import string

def generate_hashtag(s):

    words = s.split()
    words = [word.capitalize() for word in words]

    hashtag = ''.join(words)

    hashtag = ''.join(char for char in hashtag if char not in string.punctuation + ' ')

    hashtag = '#' + hashtag

    hashtag = hashtag[:140]

    return hashtag

input_str = input("Введіть рядок: ")

result = generate_hashtag(input_str)
if len(result) == 1:
    print("Хештег не може бути порожнім.")
else:
    print("Хештег:", result)