# print("Hello World")
# print("1s" * 10)
# course = print("Python \'Programming\'")
# course = print("Python \"Programming\"")
# course = print("Python \n Programming")

# first = "Joyce"
# last = "Yu"
# # full = f"{first} {last}"
# # full = f"{len(first)} {last}"
# full = f"{len(first)} {2+2}"
# print(full)

# print(10//3)
# print(bool(""))

# x = input("x: ")  # always a string
# print(type(x))  # str
# y = int(x) + 1  # float(x), bool(x), str(x)
# print(f"x: {x}, y:{y}")  # x: 1 y: 2

# print(ord("b"))

# age = 22
# message = "eligible" if age >= 18 else "not eligible"
# print(message)

# for letter in 'Python':
#     if letter == 'h':
#         # pass  # if "continue" won't print next line
#         print("This is pass block")
#     print(('Current Letter :'), letter)

# print("Good bye!")

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# count = 0
# for i in range(2, 10, 2):
#     print(i)
#     count += 1
# print(f"we have {count} even numbers")

# def greet(first_name, last_name):
#     print(f"hi {first_name} {last_name}")
#     print("welcome aboard")


# greet("Joyce", "Yu")

# def greet(first_name, last_name):
#     return f"hi {first_name} {last_name}"


# message = greet("joyce", "yu")
# file = open("content.txt", "w")
# file.write(message)

# def increment(number, by=1):
#     return number + by


# print(increment(2, by=1))

# def multiply(*numbers):  # pass variable nbr of args to function
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="john", age=22)  # auto creat dic

# message = "a"


# def greet(name):
#     global message
#     message = "b"


# greet("Mosh")
# print(message)

# def fizz_buzz(input):
#     result = input
#     if (input % 3 == 0) and (input % 5 == 0):
#         result = "Fizz_Buzz"
#     elif input % 3 == 0:
#         result = "Fizz"
#     elif input % 5 == 0:
#         result = "Buzz"
#     return result


# print(fizz_buzz(15))

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.popleft()
# print(queue)
# if not queue:  # if empty
#     print("empty")

# items = [
#     ("product1", 9),
#     ("product2", 12),
#     ("product3", 10),
# ]
# # lambda: expression, parameters
# prices1 = list(map(lambda item: items[1], items))  # map
# prices2 = [item[1] for item in items]  # list coomprehension

# filtered1 = list(filter(lambda item: item[1] >= 10, items))  # filter
# filtered2 = [item for item in items if item[1] >= 10]
# print(prices1)
# print(prices2)
# print(filtered1)
# print(filtered2)  # list coomprehension


# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip("abc", list1, list2)))

# numbers = [1, 2, 3, 4, 4, 4, 4]
# first, second, *other = numbers
# print(first)
# print(other)

# letters = ["a", "b", "c"]
# # Add
# letters.append("d")
# letters.insert(0, "-")

# # Remove
# letters.pop(0)
# letters.remove("b")
# del letters[0: 1]
# letters.clear()
# print(letters)

# letters = ["a", "b", "c"]
# print(letters.count("d"))
# if "b" in letters:
#     print(letters.index("b"))

# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters, 5):  # otherwise return object
#     print(index, letter)

# items = [
#     ("product1", 9),
#     ("product2", 12),
#     ("product3", 10),
# ]

# # solution 1:


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# # solution 2:
# items.sort(key=lambda item: item[1])  # lambda
# print(items)

# point = 1,  # tuple, if no comma then int
# point = ()  # tuple
# point = tuple("hello world")
# point = (1, 2, 3, 10)
# print(point[0:2])
# x, y, z, d = point
# if 10 in point:
#     print("exist")

# only if dealing w large data and have performance issue, otherwise use list and tuple
# from array import array
# numbers = array("i", [1, 2, 3])

# print(numbers[0])

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second) #either but not both

# if 1 in first:
#     print("yes")
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))  # get
# del point["x"]  # del
# print(point)
# for key in point:
#     print(key, point[key])  # solution 1
# for x in point.items():
#     print(x)  # return tuples
# for key, value in point.items():
#     print(key, value)  # solution 2

# values = {x * 2 for x in range(5)}  # return set
# values = {x: x * 2 for x in range(5)}  # return dict
# print(values)
# from sys import getsizeof
# values = (x * 2 for x in range(5))  # return generator object
# for x in values:  # no len need iterate
#     print(x)
# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))
# values = [x * 2 for x in range(100000)]  # return list
# print("list:", getsizeof(values))

# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

# # creating lists
# values = list(range(5))
# print(values)

# first = [1, 2]
# second = [3]
# values = [*range(5), *first, "a", *second, *"Hello"]
# print(values)

# # create dict
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)

# sentence = "this is a common interview question"
# dic = {}
# for i in range(len(sentence)):
#     # if sentence[i] == " ":
#     #     continue
#     if sentence[i] in dic:
#         dic[sentence[i]] += 1
#     else:
#         dic[sentence[i]] = 1

# char_frequency_sorted = sorted(
#     dic.items(),
#     key=lambda kv: kv[1],
#     reverse=True)
# print(char_frequency_sorted[0])
