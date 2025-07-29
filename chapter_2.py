#----------
#Chapter 2: variables, data types and operators 
#----------

x = 12
y = 43
print("x + y :", x + y)
print('x - y :', x - y)
print("x * y :", x * y)
print("x / y :", x / y)
print("x**2 :", x**2)
print("y % x :", y % x)

first_name = "Jack"
last_name = "London"
full_name = first_name + " " + last_name 
print(full_name)

length = len(full_name)
print(length)

second_char = full_name[1]
print(second_char)

substring = full_name[0:4]
print(substring)

a = True
b = True
print(a and b)
print(a or b)
print(not a)
print(x == y)
print(x != y)
print(x > y)
print(x < y)

int5 = 33
print(int5)
string5 = str(int5)
print(f"string5: {string5}, int5: {int5}")

#----------
#exercises
#----------

#ex 1
int2 = 5
float2 = 5.14
str2 = "Hello"
bool2 = True

#ex 2
user_name = "John"
total_items = 20
item_price = 5.99

#ex 3
a = 44 
"""integer"""
b = 2.72 
"""float"""
c = "Hasta la vista, Robot!" 
"""string"""
d = True 
"""bool"""

#ex 4
string3 = "911"
int3 = int(string3)

int4 = 55
string4 = str(int4)

float6 = 2.71828
int6 = int(float6)
print(int6)

#ex 5 
print(446 + 745)
print(76 * 88)
print(45 / 9)
print(56 % 5)
print(3 ** 3)

#ex 6
print(6 > 4)
print(9 < 2)
print(11 == 11)
print(1986 != 1986)

#ex 7 
print(True and False)
print(True or False)
print(not True)

#ex 8
result = 2 + 3 * 4 - 6 / 2 + 5 * 3 - 4 / 2 + 1
print(result) # 25.0
#Operator precedence 
# ()                  #Parentheses (grouping)
# x[attr], x[i], x(...), x(...)  # Subscription, slicing, function calls, etc.
# **                 # Exponentiation
# +x, -x, ~x         # Unary operators (positive, negative, bitwise NOT)
# *, /, //, %        # Multiplication, division, floor division, modulo
# +, -               # Addition and subtraction
# <<, >>             # Bitwise shift left/right
# &                  # Bitwise AND
# ^                  # Bitwise XOR
# |                 # Bitwise OR
# Comparison ops: <, <=, >, >=, ==, !=, is, is not, in, not in
# not               # Logical NOT
# and               # Logical AND
# or                # Logical OR
# Assignment: =, +=, -=, *=, /=, etc.
# lambda            # Lambda expressions (lowest precedence)

#ex 9
def area_rect(width, length):
    return width * length

print(area_rect(4, 9))

#ex 10
a = 4
b = 6
c = 8
result = a < b and b < c or a > b
print(result) #true
