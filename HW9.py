import random

random_list = random.sample(range(1, 101), random.randint(3, 10))
print("Початковий список:", random_list)

list_length = len(random_list)
new_list = [random_list[0], random_list[3], random_list[list_length - 2]]
print("Новий список:", new_list)