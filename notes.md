# Code with Mosh - Complete Python Course

## Python Language
### Primitive Types
* formatted strings
```python
first = "Joyce"
last = "Yu"
full = f"{first} {last}"
full = f"{len(first)} {2+2}"
full = f"({x},{y})"
print(full)
```

* escape sequences:

```python
course = print("Python \'Programming\'")
course = print("Python \"Programming\"")
course = print("Python \n Programming")
```
* boolean value: False, True
  * Falsy: "", 0, None

* string methods
```python
course_capital = course.upper()
string.lower()
string.title()
course = " python programming"
course.strip() #remove all blanks
.lstrip() #remove left blanks
.rstrip() #remove right blanks
.find("pro") #find index of "pro", capital sensitive -1 if not found
print("pro" in course) #return "True" or "False"
.replace("p","j") #replace "p" w "j"
print("swift" not in course) #return  "True"
```
* number methods

```python
10/3 #3.33
10//3 #3
number = 100
10 ** 3 #1000

number = 100
while number > 0:
    print(number)
    number //= 2
```
* python 3 math module:

```python
import math
print(math.ceil(2.2)) # return 3

```
* type conversion
```python
x = input("x: ") # always a string
print (type(x)) #str
y = int(x) + 1 #float(x), bool(x), str(x)
print(f"x: {x}, y:{y}") #x: 1 y: 2
```
* comparison operators
```python
ord("b") # 98
```

* ternary operator
```python
age = 22
message = "eligible" if age >= 18 else "not eligible"
print (message)
```
* defining functions
```python
def greet(first_name, last_name):
    return f"hi {first_name} {last_name}"
 
message = greet("joyce","yu")
file = open("content.txt","w")
file.write(message)
```
* keyword & default argement
```python
def increment(number, by): #by = 1 then it has default value, optional parameter should be after required parameter
    return number + by


print(increment(2, by=1))  #by = 1 is key arguments
```
* xargs
```python
def multiply(*numbers): #pass variable nbr of args to function
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
```
* xxargs
```python
def save_user(**user):
    print(user["name"])


save_user(id=1, name="john", age=22)  # auto create dictionary
```
* list unpacking
```python
numbers = [1, 2, 3, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(other)
```
* unpacking operator
```python
numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

# create lists
values = list(range(5))
print(values)

first = [1, 2]
second = [3]
values = [*range(5), *first, "a", *second, *"Hello"]
print(values)

# create dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
```
* zip
```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
```
* Global variable - bad practice
```python
message = "a"


def greet(name):
    global message # bad practice though
    message = "b"


greet("Mosh")
print(message)
```
* Add/Remove
```python
letters = ["a", "b", "c"]
# add
letters.append("d")
letters.insert(0, "-")
# remove
letters.pop(0)
letters.remove("b")
del letters[0: 1]
letters.clear()
print(letters)
```
* count/index
```python
letters = ["a", "b", "c"]
print(letters.count("d")) # count
if "b" in letters:
    print(letters.index("b")) #index
```
* enumerate 
```python
# enumerate(iterable, start=0)
letters = ["a", "b", "c"]
for index, letter in enumerate(letters, 5):#otherwise return object; 0 by default
    print(index, letter)
# output
5 a
6 b
7 c
```
* sort
```python
items = [
    ("product1", 9),
    ("product2", 12),
    ("product3", 10),
]

# solution 1:


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# solution 2:
items.sort(key=lambda item: item[1])  # lambda
print(items)
```
* deque
```python
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.popleft()
print(queue)
if not queue:  # if empty
    print("empty")
```
* list comprehension
* lambda - anonymous function
* map function
* filter function
```python
items = [
    ("product1", 9),
    ("product2", 12),
    ("product3", 10),
]
# lambda arguments: expression
prices1 = list(map(lambda item: items[1], items))  # map
prices2 = [item[1] for item in items]  # list coomprehension

filtered1 = list(filter(lambda item: item[1] >= 10, items))  # filter
filtered2 = [item for item in items if item[1] >= 10]
print(prices1)
print(prices2)
print(filtered1)
print(filtered2)  # list coomprehension
```
* tuples - immutable
```python
point = 1,  # tuple, if no comma then int
point = ()  # tuple
point = tuple("hello world")
point = (1, 2, 3, 10)
print(point[0:2])
x, y, z, d = point
if 10 in point:
    print("exist")
```
* array & python3 typecode
  * `array`: only if dealing w large data and have performance issue, otherwise use list and tuple
    ```python
    from array import array
    numbers = array("i", [1, 2, 3])

    print(numbers[0])
    ```
* set
  * `set`: unordered unique
    ```python
    numbers = [1, 1, 2, 3, 4]
    first = set(numbers)
    second = {1, 5}
    print(first | second)
    print(first & second)
    print(first - second)
    print(first ^ second)  # ^: either but not both: {2, 3, 4, 5}

    if 1 in first:
        print("yes")

    ```
* dictionary
```python
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))  # get
del point["x"]  # del
print(point)
for key in point:
    print(key, point[key])  # solution 1
for x in point.items():
    print(x)  # return tuples
for key, value in point.items():
    print(key, value)  # solution 2
```
* dictionary comprehension
```python
values = {x * 2 for x in range(5)}  # return set
values = {x: x * 2 for x in range(5)}  # return dict
print(values)
```
* generator expressions
```python
from sys import getsizeof #getsizeof
values = (x * 2 for x in range(5))  # return generator object
for x in values:  # no len, need iterate
    print(x)
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]  # return list
print("list:", getsizeof(values))
```

## Shortcut
* Windows
  
  * `end` end of line
  * `home` beginning of line
  * `cntrl home`
  * `cntrl end`
  * `alt + up/down` move lines up/down
  * `alt + shift + up/down` duplicate lines
  * `ctrl + /` convert to comment
  
* Mac
  
  * `Fn + right` end of line
  * `Fn + left` beginning of line
  * `Fn + up` end of paragraph
  * `Fn + down` beginning of para
  * `alt + option +up/down` move lines
  * `command + /` convert to comment
  

* Debugging
  * `F9` for Windows and Fn+F9 mac
  * `F5` to run
  * `F10` one line at a time/step over
  * `F11` to step into a function
  * `Shift + F11` to step out of function

* (Code) Problems

  * `Shift + Command(Ctrl if Windows) + M`
* Command Palette
  
  * `Shift + Command(Ctrl if Windows) + P`
* Run Python w:
  
  * Instead of "Python3 xxx.py"
  * Search extension for "code runner" and install ".runner", then we can run code with:
    * `Ctrl + alt + n`

  * Change "python -u" to "python3": "Code"->"Preferences"-->"Settings"-->"..."-->"Open Settings.json"-->search "code-runner.executorMap"-->change "User Settings", after last line, add "," type "code-runner.executorMap" then Enter, this will copy "default user settings" to "user settings"; then change "python":"python -u" to "python":"python3"

## Others

### Install Pip
        sudo apt install python3-pip

### Extension: PEP8 (Formatting Python Code)

* Command palette, type in "format", install PEP8
* later repeat and type in "format" will automatically correct OR
* Automatic formatting at "Save": Code --> Preferences --> Settings --> Search "Form
* at and tick "Format on Save"

### Extension: code runner
* .runner

### Extension: linter
* pylint

### Python Implementations

language: define rules, implementation: exeucute code
Python->CPython(or Jython)-->Python Bytecode(or Java Bytecode)-->Python Virtual Machine-->Machine Code

* CPython (default)
* Jython: Java
* IronPython: C#
* PyPy: subset of Python
  
