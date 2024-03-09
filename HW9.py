import random

random_list = random.sample(range(1, 101), random.randint(3, 10))
print("Початковий список:", random_list)

new_list = [random_list[0], random_list[2], random_list[1]]
print("Новий список:", new_list)
