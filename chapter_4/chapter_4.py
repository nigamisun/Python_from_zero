#-----------
#Chapter 4: Functions and modules
#-----------

def welcome(name):
    print(f"Hello my dear {name}!")

welcome("Azamat")

def square(x):
    return x**2

#print(square(3))
res = square(3)
print(res)

def add(a, b):
    return a + b

print(add(4, 5))

def Welcome1(name = "Robot"):
    print(f"Hello my dear {name}!")

Welcome1()
Welcome1(name = "Azamat")

def add1(*args):
    return sum(args)

res = add1(1, 2, 3, 4, 5)
print(res)

def welcome_person(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)

welcome_person(name="Peter", age="42", city="New Haven")

def sum_and_product(a, b):
    return a + b, a * b

print(sum_and_product(4,6))
sum1, prod = sum_and_product(4, 6)
print(sum1)
print(prod)

def something():
    print("Something!")

something()

def add3(x, y):
    res = x + y
    return res

print(add3(4, 7))

counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(increment())

# def increment1():
#     counter += 1
#     return counter
# print(increment1())

add2 = lambda x,y: x + y

print(add2(4,6))

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares)) 

print(len(numbers))
print(range(1, 5))
print(str(5))
print(int('5'))
print(float('3.14'))
print(type(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

import math
result = math.sqrt(169)
print(result)

from math import sqrt
result = sqrt(256)
print(result)

import my_own_module as my
my_login = "Azamat"
my_password = "12345"
print(my.autentification(login = my_login, password = my_password))

print(my.factoial(5))

# import os

# print(os.name)

# import datetime 

# now = datetime.now()
# print(now)

# import re 

# text = "Email: my.google@gmail.com"
# match = re.search(r"\S+@\S+\.\S+", text)
# if match:
#     print("Found mail:", match.group())

# import urllib 

# response = urllib.urlopen("https://example.com")
# html = response.read().decode("utf-8")
# print(html[:200])

# import math 

# print(math.pi)

# import random 

# print(random.randint())
# print(random.choice([1, 2, 3, 4, 5, 6]))

# import json 

# data = {"name":"Azamat", "age":24}
# json_str = json.dumps(data)
# print(json_str)

# parsed = json.loads(json_str)
# print(parsed["name"])

# import csv

# # Extract
# source_data = [
#     {"name": "Azamat", "age": 25},
#     {"name": "John", "age": 30}
# ]

# # Transform
# transformed_data = []
# for row in source_data:
#     transformed_data.append([
#         row["name"].capitalize(),
#         row["age"]
#     ])

# # Load
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerows(transformed_data)

#----------
#exercises
#----------

#ex 1
# def my_pet_color(color):
#     print(f"My pet is {color}")

# print("Enter your pets color:")
# color = str(input())
# my_pet_color(color)

#ex 2
def add4(param1, param2):
    return param1 + param2

print(add4(18,39))

#ex 3
def add5(param1 = 0, param2 = 0):
    return param1 + param2

print(add5(param1 = 18, param2= 39))

#ex 4
def greet(name = "Stranger"):
    print(f"Hi {name}...")

greet("Severa")

#ex 5
a = 1

def sum_a():
    a = 2
    return a + a

print(sum_a())
print(a)

#ex 6
x = 1934
def modify_x():
    global x
    x = 2023
    print(f"Inside the function: x = {x}")
modify_x()
print(f"Outside the function: x = {x}")

#ex 7
square1 = lambda x: x**2
print(square1(11))

#ex 9
import modul_ex_class as mec

cat = mec.My_Animal("Lily", "cat")
cat.con()

#ex 10
import my_module1 

my_module1.say_hi("Azamat")

