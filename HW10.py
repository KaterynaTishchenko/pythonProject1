import keyword
import string

variable_name = input("Введіть рядок для перевірки: ")

if variable_name in keyword.kwlist:
    print(False)
else:
    if not (variable_name[0] == '_' or variable_name[0].isalpha()):
        print(False)
    else:
        for char in variable_name[1:]:
            if char not in string.ascii_letters + string.digits + '_':
                print(False)
                break
        else:
            if variable_name.isdigit():
                print(False)
            else:
                print(True)