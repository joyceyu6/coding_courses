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

* Exceptions
```python
try:
    age = int(input("age:"))
except ValueError as ex:  # 'as ex' optional
    print("you didn't enter a valid age")
    print(ex)
    print(type(ex))
else:  # executed if no exceptions
    print("no exceptions were thrown")
print("execution continues")
```
```python
try:
    age = int(input("age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError): #exceptions
    print("you didn't enter a valid age")
else:
    print("no exceptions were thrown")
```
```python
try:
    with open("app.py") as file:  # automatically release resources no need for the 'finally' clauses
        print("file opened")
        # file.__exit__  # for demo only: contacts mgt protocol if it has "enter" and "exit" when type '._'we can use "with"
    age = int(input("age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("no exceptions were thrown")
# finally:  # always executed to release extra resources
#     file.close #no need if using "with"
```
```python
# define your own exceptions - costly, comparison as below
# search python3 built-in exceptions
from timeit import timeit #timeit to compare
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error) #change to "pass"
    
"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code", timeit(code1, number=10000)
      )  # execute 10k times and return time
print("second code", timeit(code2, number=10000)
      )
```
* Classes
```python
# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack
class Point:
    def draw(self):  # at least one parameter
        print("draw")


point = Point()
point.draw  # inheritance
print(type(point))  # '<class '__main__.Point'>
print(isinstance(point, Point))  # isinstance
```
```python
# constructors: so we can supply initial values
# class vs. instance attributes
# magic methods: __init__,__str__ etc.

class Point:
    default_color = "red"  # class level attribute

    def __init__(self, x, y):  # self is a reference to the Point object
        self.x = x  # instance attribute - attrribute that belong to Point objects
        self.y = y

    @classmethod  # decorator for class method
    def zero(cls):  # convention for the 1st parameter, can call anything
        return cls(0, 0)

    def __str__(self):  # magic method
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")  # method that read attributes


point = Point(1, 2)  # instance attributes
Point.default_color = "yellow"  # change visible to all type
print(Point.default_color)  # class attribute
print(point.default_color)  # instance attribute
point.draw()  # methods such as draw, attributes such as x, y

point = Point(0, 0)
point = Point.zero()  # class level method
point.draw()

# search python3 magic methods, e.g: __str__(self)
point = Point(1, 2)
print(point.__str__)  # magic method from inheritance
print(str(point))  # defined by ourselves
```
```python
# performaing arithmetic operations w magic methods
# Comparing objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # ref magic methods online page
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):  # ref magic methods online page
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point > other)  # Pyton will automatically figure out less operator
combined = point + other  # return object
print(combined.x)
```
```python
# creating custom containers
class TagCloud:
    def __init__(self):  # define constructure
        self.tags = {}

    def add(self, tag):
        # 'get' method w a default value:
        self.tags[tag.lower()] = self.tags.get(
            tag, 0) + 1  # not case sensitive

    def __getitem__(self, tag):  # getitem is read only - 'set' to write
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)  # built-in iteration function


cloud = TagCloud()
cloud["python"]
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(cloud["python"])  # use __getitem__ to define; return 3
cloud["python"] = 10  # use __setitem__ to define, return 10
print(cloud["python"])
print(len(cloud))  # use __len__ to define
print(iter(cloud))  # return iterable object
print(next(iter(cloud))) #return 'python'
```
```python
# private members
# `F2 ` --> chg 'tags' to '__tags'-->refactory libary rope install
# __dict__ will still show, no real privacy
class TagCloud:
    def __init__(self):  # define constructure
        self.__tags = {}  # hide attributes from outside

    def add(self, tag):
        # 'get' method w a default value:
        self.__tags[tag.lower()] = self.__tags.get(
            tag, 0) + 1  # not case sensitive

    def __getitem__(self, tag):  # getitem is read only - 'set' to write
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)  # built-in iteration function


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
# will crash as everything stored as lower case, hide key from access
print(cloud.__tags)  # exception/error, and no '.' attribute any more
print(cloud.__tags["PYTHON"])  # exception/error
# technically is still accessible:
# dictionary that holds all attributes, return {'_TagCloud__tags': {'python': 1}}
print(cloud.__dict__)
print(cloud._TagCloud__tags)  # still accisible: return {'python': 1}
```
```python
# set property - ref solution 3
# problem: no negative price input

# solution1: not best python practice:


class Product:
    def __init__(self, price):
        self.set__price(price)

    def get__price(self):
        return self.__price

    def set__price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(-50)  # throw error
```
```python
# solution2: define property: looks like a regular attributes but internally has two methods getter and setter
# this solution still has get_price and set_price when input '.'
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get__price(self):
        return self.__price
   
    def set__price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # 4 optional parameters: fget,fset,fdel, doc
    price = property(get__price, set__price)


product = Product(10)
product.price = -10  # throw error, define w property
print(product.price)
```
```python
# solution3: define property w decorator
# use decorator insteae of .__

class Product:
    def __init__(self, price):
        self.price = price

    @property  # automatically create price property
    def price(self):
        return self.__price

    @price.setter  # if without .setter cannot change value afterwards
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(-10)
print(product.price)
```
```python
# inheritance
# DRY: don't repeat yourself
class Animal:  # parent/base class
    def __init__(self):  # constructor
        self.age = 1  # age attributes

    def eat(self):
        print("eat")


class Mammal(Animal):  # child/sub class
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
```
```python
# inheritance
# DRY: don't repeat yourself
class Animal(object):  # parent/base class, same as 'class Animal'
    def __init__(self):  # constructor
        self.age = 1  # age attributes

    def eat(self):
        print("eat")


class Mammal(Animal):  # child/sub class
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Animal)) #isinstance
# mammal from animal from object
o = object()
print(issubclass(Mammal, Animal)) #issubclass
```
```python
# method overriding - replacing or extending a method defined in base class
# extend only with 'super().__init__() ', otherwise override
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # print 'Animal Constructor" first:
        # super().__init__()  # avoid method overriding
        print("Mammal Constructor")
        self.weight = 2
        # print 'Mammal Constructor" first:
        super().__init__()  # avoid method overriding

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)  # error if w/o super().__init__()'as what we difined in mammal overrode what's in base class
print(m.weight)
```
```python
# issue(1): multi-level inheritance: don't go beyond two levels
# issue(2): multi inheritance: look for base class definition first; complicated when things have common
# good example: multi inheritance if exclusive, e.g., fly, swim, then a class w both fly and swim

# good example: model a stream of data, depending type of string
# (1) no multi-level inheritance: only one/two level
# (2) no multi inheritance:sub class doesn't have multiple parents
# create custom exeption with inheriting from Exception class
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            # custom exception as no built-in in Python
            raise InvalidOperationError("stream already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")
```
```python
# abstract base classes: provide common code through derivatives
# issue 1: what Stream is it? should not be able to create directly an instance of Stream class
# issue 2: no way to create common interface across differnt kind of Streams
# example and solution:
from abc import ABC, abstractclassmethod  # import abstractclassmethod

class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # step1: derive ABC class to make it abstract
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            # custom exception as no built-in in Python
            raise InvalidOperationError("stream already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream already closed")
        self.opened = False

    # step2: define a read method:
    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")


class MemoryStream(Stream):
    # pass  # aslo considered abstract unless implement below read method:
    def read(self):
        print("reading data from a memory stream")


stream = Stream()  # get type error after use abstract base case
stream.open()

stream = MemoryStream()
stream.open()  # get type error if w/o define read method
```
```python
# polymorphism: many forms
# Example: below 'draw' method taking many forms defined ad vante
from abc import ABC, abstractclassmethod


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):  # polymorphism
    for control in controls:
        control.draw()


ddl = DropDownList()
print(isinstance(ddl, UIControl))  # return True
# draw(ddl)  # return DropDownList
textbox = TextBox()
# draw(textbox)  # return TextBox
# rendering entire form:
draw([ddl, textbox])  # return "DropDownList" and "TextBox"
```
```python
# duck typing & polymorphism: Python doesn't check types
# e.g. below w/o UIControl python can still iterate as long as each has 'draw' method
class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):  # polymorphism, as long as iterable
    for control in controls:
        control.draw()


ddl = DropDownList()
# draw(ddl)  # return DropDownList
textbox = TextBox()
# draw(textbox)  # return TextBox
# rendering entire form:
draw([ddl, textbox])  # return "DropDownList" and "TextBox"
```
```python
# extending built-in types
class Text(str):  # inherit python string
    def duplicate(self):
        return self+self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)  # extend Append method


text = Text("Python")
print(text.duplicate())
list = TrackableList()
list.append("1")
```
```python
# Data Classes
# solution 1 w magic methods, without data class:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
```
```python
# Data Classes
# solution 2 with data class(e.g.namedtuple):
from collections import namedtuple  # namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)  # has attributes like in regular classes, not mutable though
p2 = Point(x=1, y=2)
print(p1 == p2)
```
* Modules
```python
# write in app.py to import sales.py functions
# alternative 1
from sales import calc_shipping, calc_tax  # all functions in sales.py
# dont import * to run the risk of overriding functions
calc_shipping()
calc_tax()
```
```python
# alternative 2
import sales
sales.calc_shipping()  # alternative

# complied python files to speed up file loading, not actual performance
```
* pacakges - containter for one or more modules
    * `__init__.py`: # treat folder as packages, file mapped to directory and a module is mapped to a file
    ```python
    # packages
    # organize modules to sub-directories

    # create __init__.py under commerce folder
    # sales.py under ecommerce folder:
    def calc_tax():
    pass

    def calc_shipping():
    pass
    ```
    ```python
    # option 1: app.py:
    import ecommerce.sales
    ecommerce.sales.calc_tax
    ```
    ```python
    # option 2: app.py:
    from ecommerce.sales import calc_tax,calc_shipping
    calc_tax()
    ```
    ```python
    # option 3: app.py:
    from ecommerce import sales  # import sales module as object
    sales.calc_shipping  # use '.'method to access all members of the module
    ```
* sub-packages
```python
# create shpping folder and move sales there
# create `__init__.py` under shopping
# app.py:
from ecommerce.shopping import sales
```
* intra-package references
```python
# add customer package w contact.py under ecommerce
# in sales.py:
# absolute import - recommended:
from ecommerce.customer  import contact
# relative import:
from ..customer import contact
```
* the dir function
```python
from ecommerce.shopping import sales
print(dir(sales))
'''
returns ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax']
'''
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
```
* executing modules as scripts
```python
#.py:
from ecommerce.shopping import sales
'''
return:
ecommerce initialized
sales initialized ecommerce.shopping.sales
'''
```
```python
#ecommerce-->__init__.py:
print("ecommerce initialized")
```
```python
# sales.py:
# executing modules as scripts
# load once and cache
print("sales initialized", __name__)  # __name__
# command + p or cntl + p windows to switch programs
print("Sales")


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":  # only if run by this own module
    print("sales started")
    calc_tax()
'''return:
sales initialized __main__
Sales
sales started
'''
```

 * Python Standad Library - Files
    * Paths
        ```python
        # search Python3 pathlib
        from pathlib import Path
        # creat Path object in a few different ways:
        Path("C:\\Program Files\\Microsoft")
        Path(r"C:\Program Files\Microsoft")  # windows raw string
        Path("/usr/local/bin")  # mac
        Path()  # current folder
        Path("ecommerce/__init__.py")
        Path()/Path("ecommerce")  # combine paths
        Path()/"ecommerce"/"__init__.py"  # combine path w string
        Path.home()  # home directory

        path = Path("ecommerce/__init__.py")
        path.exists()
        path.is_file()
        path.is_dir()
        print(path.name)
        print(path.stem)
        print(path.suffix)
        print(path.parent)
        path = path.with_name("file.txt")  # only name and extension of the file
        print(path)
        print(path.absolute())
        path = path.with_suffix(".txt")
        print(path)
        '''
        return:
        __init__.py
        __init__
        .py
        ecommerce
        ecommerce/file.txt
        /home/joyce/coding_courses/ecommerce/file.txt
        ecommerce/file.txt
        ```
    * Directories
    ```python
    # cannot search recursively or by a pattern
    paths = [p for p in path.iterdir() if p.is_dir()]
    print(paths)
    '''return
    [PosixPath('ecommerce/__pycache__'), PosixPath('ecommerce/customer'),
            PosixPath('ecommerce/shopping')]
    '''
    # .glob: search by a pattern:
    paths = [p for p in path.iterdir() if p.is_dir()]
    py_files = [p for p in path.glob("*py")]  # .glob
    print(py_files)
    '''return
    [PosixPath('ecommerce/__init__.py')]
    '''
    # .rglob - search recursively
    paths = [p for p in path.iterdir() if p.is_dir()]
    # option1:
    py_files = [p for p in path.glob("**/*.py")]  # .glob
    print(py_files)
    # option2:
    py_files = [p for p in path.rglob("*.py")]  # recursive .glob
    print(py_files)
    '''return
    [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer/__init__.py'), PosixPath('ecommerce/customer/contact.py'), PosixPath('ecommerce/shopping/__init__.py'), PosixPath('ecommerce/shopping/sales.py')]
    '''
    ```
    * Files
    ```python
    from pathlib import Path
    from time import ctime
    path = Path("ecommerce/__init__.py")
    # path.exists()
    # path.rename("init.txt")
    # path.unlink()  # delete link
    print(path.stat())  # info of the file
    print(ctime(path.stat().st_ctime))  # creation time of the file
    path.read_bytes()  # binary data
    with open(path, "r") as file:
        print("file opened")
    print(path.read_text())  # content of the file
    path.write_text("new code")
    # path.write_bytes()
    ```
    ```python
    # copy source file content to target file
    # option 1: write_text
    from pathlib import Path
    source = Path("ecommerce/__init__.py")
    target = Path()/"__init__.py"

    target.write_text(source.read_text())
    ```
    ```python
    # option 2: shutil
    import shutil
    from pathlib import Path
    source = Path("ecommerce/__init__.py")
    target = Path()/"__init__.py"
    shutil.copy(source, target)
    ```
    * Zip Files
    ```python
    from pathlib import Path
    from zipfile import ZipFile
    zip = ZipFile("files.zip", "w") #zip
    with ZipFile("files.zip", "w") as zip:
        for path in Path("ecommerce").rglob("*.*"):  # rglob
            zip.write(path)
    with ZipFile("files.zip") as zip:
        print(zip.namelist())  # all files name
        info = zip.getinfo("ecommerce/__init__.py")
        print(info.file_size)
        print(info.compress_size)
        zip.extractall("extract")  # extract to "extract" directory
    ```
    * CSV Files
    ```python
    import csv
    with open("data.csv", "w") as file:
        writer = csv.writer(file)  # write object
        writer.writerow(["transaction_id", "product_id", "price"])
        writer.writerow([1000, 1, 5])
        writer.writerow([1001, 2, 15])

    with open("data.csv") as file:  # read
        reader = csv.reader(file)
        # print(list(reader))  # return list of list and position to end of file
        for row in reader:
            print(row)
    ```
    * JSON Files
    ```python
    import json
    from pathlib import Path
    movies = [
        {"id": 1, "title": "Terminator", "year": 1989},
        {"id": 2, "title": "Kindergarten Cop", "year": 1993}
    ]

    # write data to json file
    data = json.dumps(movies)
    print(data)
    Path("movie.json").write_text(data)

    # read json file
    data = Path("movie.json").read_text()
    movies = json.loads(data)
    print(movies[0]["title"])
    ```
* Python Standad Library - SQLite
```python
    '''error:
    install sqlite browser failed
    '''
    
    # create database
    import sqlite3
    import json
    from pathlib import Path
    movies = json.loads(Path("movies.json").read_text())
    with sqlite3.connect("db.sqlite3") as conn:
        command = "INSERT INTO Movies VALUES(?,?,?)"  # placeholders
        for movies in movies:
            conn.execute(command, tuple(movie.values())  # pass actual values
        conn.commit()
        ''''sqlite browser
        create movies table first
        search"db browser for sqlite"
        download "DB Browser for SQLite"
        create table "movies" w 3 columns
        Id: make it "PK" primary key, integer
        Title: text
        Year: integer
        "Not": check so cannot be null
        '''
        '''
        # install sqlite in Ubutun and then in command line:
        sqlite3 db.db
        sqlite> create table movies(Id INTEGER, Title VARCHAR(100), year INTEGER)
        ...> ;
        sqlite> .quit
        '''
```
```python
    # read data from database:
    import sqlite3
    import json
    from pathlib import Path

    with sqlite3.connect("db.sqlite3") as conn:
        command="SELECT * FROM Movies"
        cursor=conn.execute(command)  # return cursor, an iterable object
        cursor=conn.execute(command)
        # for row in cursor: #to end of cursor
        #     print(row)
        movies=cursor.fetchall()
        print(movies)
```
* Python Standad Library - Date Time
    * Timestamps
    ```python
    #use time
    # timeit is another option
    import time
    print(time.time())  # not readable, used for calculations


    def send_emails():
        for i in range(10000):
            pass


    start = time.time()
    send_emails()
    end = time.time()
    duration = end - start
    print(duration)
    ```
    * Date/Time
    ```python
        from datetime import datetime
        import time

        dt1 = datetime(2018, 1, 1)
        dt2 = datetime.now()
        # strptime: parsing or converting datetime strings
        dt3 = datetime.strptime("2018/01/01", "%Y/%m/%d")  # 'y%' for 2 digit year
        # search python3 strptime, see "directive"
        dt = datetime.fromtimestamp(time.time())
        print(dt)
        print(dt3)
        print(f"{dt.year}/{dt.month}")
        # strftime - convert to string
        print(dt.strftime("%Y/%m"))
        print(dt1 > dt2)
    ```
    * Time Deltas
    ```python
    from datetime import datetime, timedelta  # timedelta
    dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
    print(dt1)
    dt2 = datetime.now()
    duration = dt2 - dt1
    print(duration)
    print("days", duration.days)
    print("seconds", duration.seconds)  # seconds after days
    print("total_seconds", duration.total_seconds())  # total_second() method
    ```
* Python Standad Library - Randome Values
```python
import random  # random
import string  # string
print(random.random())
print(random.randint(1, 10))
print(random.choices([1, 2, 3, 4], k=2))  # return 2 randoms
print(random.choices("abcdefghi", k=4))  # return list
print("".join(random.choices("abcdefghi", k=4)))  # return string
print(string.ascii_letters)  # all leters upper and lower cases
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)  # 0 to 9
# ramdom 4 numbers:
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))
# shuffle numbers
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
```
* Python Standad Library - Open Browser
```python
# open browser at the end of deployment
import webbrowser
print("Deploy completed")
webbrowser.open("http://google.com")
```
* Python Standad Library - Emails
    * send email w pain text and image
    ```python
    # send emails w image and text
    # email pacckage
    # mime: sub package mime defining format of emails
    # multipart package has MIMEMultipart object, incl both plain/html content
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText  # MIMEText class to set body
    from email.mime.image import MIMEImage
    import smtplib
    from pathlib import Path

    message = MIMEMultipart()
    message["from"] = "Joyce Yu"
    message["to"] = "yumengnan@gmail.com"
    message["subject"] = "this is a test"
    message.attach(MIMEText("Body", "plain"))  # payload, can add "html", text
    message.attach(MIMEImage(Path("joyce.png").read_bytes()))  # image

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()  # hello message/greeting to smtp server part of smtp protocol
        smtp.starttls()  # ttl: transport level security
        smtp.login("joyce.mn.yu@gmail.com", "003965254")  # acct and psw
        smtp.send_message(message)
        print("Sent...")
    ```
    * send emails w html template
    ```python
    # send emails w html template:
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from pathlib import Path
    from string import Template  # template
    template = Template(Path("template.html").read_text())  # template.html

    message = MIMEMultipart()
    message["from"] = "Joyce Yu"
    message["to"] = "yumengnan@gmail.com"
    message["subject"] = "this is a test"
    # substitute method will return string:
    body = template.substitute({"name": "John"})  # pass dictionary
    body = template.substitute(name="John")  # or pass keyword arg
    message.attach(MIMEText(body, "html"))  # chg to html
    message.attach(MIMEImage(Path("joyce.png").read_bytes()))  

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()  
        smtp.starttls()  
        smtp.login("joyce.mn.yu@gmail.com", "003965254")  
        smtp.send_message(message)
        print("Sent...")
    ```
    ```html
    <!-- type '!' then tab -->
    <!DOCTYPE html>
    <html lang="en">

    <head>
    </head>

    <body>
        Hi <strong>$name</strong> , this is our test email
    </body>

    </html>
    ```
* Python Standard Libarary - command-line arguments
```python
import sys
print(sys.argv)
'''terminal: return array of items:
joyce@joycey-w1:~/coding_courses$ python3 app.py -a -b -c
['app.py', '-a', '-b', '-c']
'''
if len(sys.argv) == 1:  # if no arg
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
'''terminal:
joyce@joycey-w1:~/coding_courses$ python3 app.py
['app.py']
USAGE: python3 app.py <password>
joyce@joycey-w1:~/coding_courses$ python3 app.py 12345
['app.py', '12345']
Password 12345
'''
```
* Python Library - running external programs
```python
# ls  # mac or linux
# dir  # windows

import subprocess

'''
# there are better methods than below ones:
subprocess.run
subprocess.call
subprocess.check_call
subprocess.check_output
subprocess.Popen
'''
result = subprocess.run(["ls", "-l"])  # details of current files/directories
print(type(result))
'''return
<class 'subprocess.CompletedProcess'>
'''
completed = subprocess.run(["ls", "-l"]) # output on terminal
output will not be printed on terminal but available in 'stdout' attribute:
completed = subprocess.run(["ls", "-l"], capture_output=True,text=True)
```

```python
import subprocess
# check error option 1 w try/except:
try:
    completed = subprocess.run(["python3", "other.py"],
                               capture_output=True, text=True)
    print("args", completed.args)
    print("returncode", completed.returncode)  # 1 for error
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)

# check error option 2:
if completed.returncode != 0:
    print(completed.stderr)
# check error option 3 check=True:
completed = subprocess.run(["python3", "other.py"],
                           capture_output=True, text=True, check=True)
```
* Python (Non-standard) Package Index & Virtual Environment:
    * Online libarary: [pypi](https://pypi.org)
    * Pip
    ```
    pip3 install requests
    pip install --upgfrade pip
    pip3 list 
    pip3 install requests ==2.9.0

    pip3 uninstall requests
    pip3 install requests==2.9.*
    pip3 install requests~=2.9.0

    pip3 uninstall requests
    pip3 install requests==2.*
    ```

    ```python
    '''error:
    request module not found
    '''
    import requests
    response = requests.get("http://google.com")
    print(response)
    ```
    * virtual environment
    ```python
    '''
    use Pipenv instead - see next section
    '''
    python3 -m venv env #named as env
    source env/bin/activate #mac/linux
    env/bin/activate #windows
    pip3 install requests == 2.9.* #install an earlier version in env
    deactivate
    ```
    * Pipenv
    ```python
    '''combine Pip and virtual env to a single chain
    equivalent of npm in Python
    '''
    pip3 install pipenv #delete env folder from prior section
    pipenv install requests #Pipfile, Pipfile.lock
    pipenv --venv #show venv directory, different from project directory
    pip3 uninstall requests # uninstall global requests
    python3 app.py '''return No module named'requests'''
    pipenv shell #activate virtual environment of the project
    python3 app.py #new works
    exit # deactivate venv
    ```
    * Virtual Environments in VSCode
    ```python
    '''tell VScode to run program in venv'''
    pipenv --venv #find venv directory
    # VSCode settings:
    # (1) "code-runner.executorMap":{"python":"..."} replace w 'pipenv --venv's result
    # (2) "python.pythonPath":".." replace w python3 path('pipenv --venv's result plus python3 subfolder) in venv
    '''VSCode settings: 
    go to code menu-->preferences-->settings in VSCode
    settings.json-->user settings
    "code-runner.executorMap":{"python":"..."} replace w pipenv --venv result
    '''
    '''
    fix issue: cannot find request module- need tell VSCode which Python interpreter to use;
    use the python3 in virtual environment in user settings:
    "python.pythonPath":".." replace w python3 path in venv
    '''
    ```
    * Pipfile
    ```python
    '''demo: delete dependencies then recrate'''
    # Pipfile will show the settings and packages
    # Pipfile.lock shows dependencies and versions
    pipenv --venv #copy path
    rm -rf ... #'...' for the above path in max or linus
    pipenv --venv #no virtual env created now
    pipenv install #install all dependencies of our app
    pipenv --venv #dependencies back
    ```
    ```python
    '''if want to install exact dependencies as pipfile.lock'''
    pipenv install --ignore-pipfile
    ```
    * Managing Dependencies
    ```python
    pipenv graph # to see list of all dependencies
    pipenv uninstall requests
    pipenv graph #no more requests but dependencies still there, however they won't be implemented in another machine as no reference to them
    pipenv install requests==2.9.* #older version installed
    '''to see outdated versions w warnings as newer version may not be compaitible:'''
    pipenv update --outdated 
    '''go to pipfile, change requets = "==2.*", then no warnings'''
    pipenv update requests # now all dependencies up to date
    ```
    * Publishing Packages
    ```python
    '''go to pypi.org, create new account
    '''
    # install 3 tools globally:
    pip3 install setuptools wheel twine 
    mkdir moshpdf
    cd moshpdf
    code .
    '''
    moshpdf folder, data folder, tests folder,setup.py,README.md,LICENSE(ref choosealicense.com)
    '''
    '''under moshpdf add __init__.py, pdf2text.py,pdf2image.py'''
    # make sure to chagne python interpretor"
    '''setup.py:'''
    import setuptools
    from pathlib import Path
    setuptools.setup(
        name = "moshpdf",
        version = 1.0,
        long_description=Path("README.md").read.text(),#from readme
        packages = setuptools.find_packages(exclude =["tests","data"])#auto find, excl. two folders

    )
    ```
    ```python
    # generate a distribution package in terminal
    python3 setup.py sdist bdist_wheel #source/build distribution packages, both zip files
    '''now under moshpdf has a build and dist foler, under dist has a source and a build zip file'''
    twine upload dist/* #upload to pypi.org
    ```
    ```python
    '''terminal:'''
    pipenv install moshpdf
    ```
    ```python
    '''python script now can use that package'''
    from moshpdf import pdf2text
    pdf2text.convert()
    ```
    * Docstrings
    ```python
    # document module and functions
    # pdf2text.py:
    """One line description.

        A more detailed explanation.
    """
    def convert():
        print("pdf2text")
    ```
    ```python
    # onelihne docstring in pdf2text.py:
    """This module provides functions to convert a PDF"""
    class Converter:
        """A simple converter for converting PDFs to text"""
        def convert(self, path):
            """
            Convert the given PDF to text.

            Parameters:
            path(str): the path to a PDF file

            Returns:
            str: the content of the PDF file as text
            """
            print("pdf2text")
    ```
    * Pydoc
    ```python
    # documentation for modules
    '''terminal:'''
    pydoc math #windows
    pydoc3 math #mac or linux
    '''copy paste the link to the doc online'''
    # if ":" pressing space to next page"
    pydoc3 moshpdf.pdf2text
    pydoc3 -w moshpdf.pdf2text #generate html of doc
    pydoc3 -p 1234 #load doc a webserver w a port, can see other modules as well
    ```
* API & Popular Python Packages
    * Yelp
    ```python
    import requests
    url = "http://api.yelp.com/v3/businesses/search"
    api_key = "xxxxx"
    headers = {
        "Authorization": "username" + api_key
    }
    params = {
        "term": "Barber",
        "location": "NYC"
    }
    response = requests.get(url, headers=headers, params=params)
    businesses = response.json()["businesses"]
    print(businesses)  # a list of dictionaries, each has id, alias,name etc
    for business in businesses:
        print(business["name"])

    # list comprehension to filter highest ratings
    names = [business["name"]
            for business in businesses if business["rating"] > 4.5]
    print(names)
    ```
    ```python
    # create config.py and move api_key there, in app.py:
    headers = {
        "Authorization": "username" + config.api_key
    }
    # .gitignore and add config.py
    ```
    * Twilio - sending text messages
    ```python
    '''pipenv install twilio'''
    # app.py:
    from twilio.rest import Client
    account_sid = "xxxx"
    auth_token = "xxxx"

    client = Client(account_sid, auth_token)
    call = client.messages.create(
        to="...",
        from_="...",  # twilio number
        body="this is our first message"
    )
    ```
    * Web Scrapping - beautifulsoup
    ```python
    '''in terminal under virtual env:'''
    pipenv install beautifulsoup4
    pipenv install requests
    ```
    ```python
    '''in app.py'''
    import requests
    from bs4 import BeautifulSoup
    response = requests.get("http://stackoverflow.com/questions")
    soup = BeautifulSoup(response.text, "html.parser")  # return object
    questions = soup.select(".question-summary")  # return a list
    print(questions[0].attrs)  # attributes
    print(questions[0].get("id", 0))
    print(questions[0].select(".question-hyperlink"))  # return list of object
    # return title of first question:
    print(questions[0].select_one(".question-hyperlink").getText())
    # return all questions on page 1 and vote for each questions:
    for question in questions:
        print(question.select_one(".question-hyperlink").getText())
        print(question.select_one(".vote-count-post").getText())
    # find pagenation if need multiple pages
    ```
    * Browser Automation - selenium
    ```python
    '''in terminal and virtual env:'''
    pipenv install selenium
    ```
    ```python
    '''go to selenium Pypi: manually download chromedriver'''
    cp chromedriver /usr/local/bin #linux/mac, or C drive if windowns 
    ```
    ```python
    '''search selenium with Python for more details: 
    Waits and Page Objects section recommended'''
    '''in app.py after selecting the virtual env:'''
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get("http://github.com")  # open website
    signin_link = browser.find_elememnt_by_link_text("Sign in")
    signin_link.click()  # on sign-in page
    username_box = browser.find_element_by_id("login_field")
    username_box.send_keys("xxxx")
    passwordbox = browser.find_element_by_id("password")
    password_box.send_keys("xxxx")
    password_box.submit()

    assert "xxxx" in browser.page_source  # exception if username not in string
    # alternatively:
    profile_link = browser.find_element_by_class_name("user-profile-link")
    link_label = profile_link.get_attribute("innerHTML")
    assert "xxxx" in link_label

    browser.quit()
    ```
    * PDFs
    ```python
    '''terminal under virtual env'''
    pipenv install pypdf2
    ```
    ```python
    # rotate and write PDF:
    import PyPDF2
    with open("first.pad", "  # rb") as file: # rb - read w binary
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        reader.getPage(0)  # return page object
        # rotate and write PDF:
        page.rotateClockwise(90)  # only rote in memory
        writer = PyPDF2.PdfFileWriter()
        # writer.addPage(page)
        # writer.insertPage(page, 1)
        # writer.insertBlankPage()
        writer.addPage(page)
        with open("rotated.pdf", "wb") as output:  # wb - write binary
            writer.write(output)
    ```
    ```python
    # merger two PDFs
    import PyPDF2
    merger = PyPDF2.PdfFileMerger()
    file_names = ["first.pd", "second.pdf"]
    for file_name in file_names:
        merger.append(file_name)
    merger.write("combined.pdf") #string as name of pdf
    ```
    * Excel Spreadsheets
    ```python
    '''terminal in virtual env:'''
    pipenv install openpyxl
    '''select virtual environment'''
    ```
    ```python
    '''app.py:'''
    wb = openpyxl.Workbook()
    openpyxl.load_workbook("transactions.xlsx")
    print(wb.sheetnames)

    sheet = wb["Sheet1"]  # case sensitive
    wb.create_sheet("Sheet2", 0)  # index before 1st sheet
    wb.remove_sheet(Sheet2)

    # Cell reference - option 1:
    cell = sheet["a1"]
    print(cell.value)
    cell.value = 1
    print(cell.row)  # 1
    print(cell.column)  # A
    print(cell.coordinate)  # A1

    # Cell reference option2:
    sheet.cell(1, 1)  # row=1, column=1
    sheet.cell(row=1, column=1)

    # iterate rows/columns:
    print(sheet.max_row)
    print(sheet.max_column)
    for row in range(1, sheet.max_row + 1):  # +1 to access last row
        for column in range(1, sheet.max_column + 1):
            cell = sheet.cell(row, column)
            print(cell)

    # reference cells:
    column = sheet["a"]
    print(column)  # return tuples
    cells = sheet["a:c"]  # return tuple of tuples
    print(cells)
    cells = sheet["a1:c3"]
    cells = sheet[1:3]  # all the cells in row 1 to row 3
    sheet.append([1, 2, 3])  # append
    sheet.insert_rows()
    sheet_insert_columns()
    sheet_delete_cols()
    sheet_delete_rows()

    wb.save("transactions.xlsx")  # save
    ```
    *   NumPy - scientific computations
    ```python
    '''terminal virtual env'''
    pipenv install numpy
    ```
    ```python
    import numpy as np

    array = np.array([1, 2, 3])
    print(array)  # return instance of numpy.ndarray
    array = np.array([1, 2, 3], [4, 5, 6])
    print(array)  # return matrix
    print(array.shape)  # return tuples(2,3)
    array = np.zeros((3, 4))  # matrix of 3 rows and 4 columns w zeros
    print(array)
    array = np.zeros((3, 4), dtype=int)  # default type integer
    array = np.ones((3, 4), dtype=int)
    array = np.full((3, 4), 5, dtype=int)
    array = np.random.random((3, 4))
    print(array[0, 0])  # vs. array[0][0] if use list
    print(array > 0.2)  # array of boolean values
    print(array[array > 0.2])  # a new array w only values>0.2
    print(np.sum(array))  # sum of array
    print(np.floor(array))  # new array w floor of each number
    print(np.ceil(array))
    print(np.round(array))

    # mathimatical operations
    first = np.array([1, 2, 3])
    second = np.array([1, 2, 3])
    print(first + second)
    print(first + 2)

    # convert inch to cm - numpy
    dimensions_inch = np.array([1, 2, 3])
    dimensions_cm = dimensions_inch * 2.54
    print(dimensions_cm)

    # convert inch to cm - pure python
    dimensions_inch = np.array([1, 2, 3])
    dimensions_cm = [x * 2.54 for x in dimensions_inch]
    ```
* Building Web Applications w Django

* command query sepration principle
```python
# violation of command query separation principle
# ask question should not change answers
# method/functions either be queries or command
import openpyxl
wb = openpyxl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
for row in range(1, 10):
    cell = sheet.cell(row, 1)  # query method should raise an exception
    print(cell.value)
sheet.append([1, 2, 3])  # add after blank rows
wb.save("transaction2.xlsx")
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
  * `command + p` to switch programs in VS
  * `command + r` to refresh page
  
* Mac
  
  * `Fn + right` end of line
  * `Fn + left` beginning of line
  * `Fn + up` end of paragraph
  * `Fn + down` beginning of para
  * `alt + option +up/down` move lines
  * `command + /` convert to comment
  * `ctrl + p` to switch programs in VS
  * `ctrl + r` to refresh page
  

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
  
