number = int(input("Введіть 5-ти значне число: "))

print(number % 10, end='')
print((number % 100) // 10, end='')
print((number % 1000) // 100, end='')
print((number % 10000) // 1000, end='')
print(number // 10000)