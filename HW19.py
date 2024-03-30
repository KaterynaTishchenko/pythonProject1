import string

def is_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char not in string.punctuation + ' ')
    reversed_text = clean_text[::-1]

    return clean_text == reversed_text

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
