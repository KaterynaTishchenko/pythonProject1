import random

def common_elements():

    multiples_of_3 = random.sample(range(3, 101, 3), random.randint(1, 10))

    multiples_of_5 = random.sample(range(5, 101, 5), random.randint(1, 10))

    common_set = set(multiples_of_3) & set(multiples_of_5)

    print("Список чисел, кратних 3:", multiples_of_3)
    print("Список чисел, кратних 5:", multiples_of_5)

    return common_set

result = common_elements()
print("Спільні елементи:", result)
