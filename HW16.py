def say_hi(name, age):
    return "Hi! My name is {} and I'm {} years old.".format(name, age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
result = say_hi(name, age)
print(result)