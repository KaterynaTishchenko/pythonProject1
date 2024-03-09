def multiply_digits(num):
    product = 1
    while num >= 9:
        temp_product = 1
        while num > 0:
            digit = num % 10
            if digit != 0:
                temp_product *= digit
            num //= 10
        product = temp_product
        num = product
    return product

number = int(input("Введіть ціле число: "))

result = multiply_digits(number)
print(result)
