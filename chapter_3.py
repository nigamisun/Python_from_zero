#-----------
#Chapter 3: Control structures: conditional statements and loops
#-----------

x = 0
if x <= 3: 
    print("x is less than or equal to 3")
else: 
    print("x is greater than 3") 

x = 3
if x > 3:
    print("x is greater than 3")
elif x < 3:
    print("x is less than 3")
else:
    print("x is equal to 3")

colors = ["green", "yellow", "red"]
for color in colors:
    print(color)

x = 0

while x < 10:
    print(x)
    x += 1

print()
for i in range(1,10):
    if i % 2 == 0:
        continue
    elif i == 1:
        pass
    elif i == 9:
        break
    else:
        print(i)

animals = ["cat", "dog", "cow", "horse"]
colors = ["black", "white", "orange", "grey"]

for animal in animals:
    for color in colors:
        if animal == "cat":
            if color == "white":
                print(f"My {animal} is {color}, and it has 3 kitens")
            elif color == "orange":
                print(f"My {animal} is {color}, and it is very friendly")
            else: 
                print(f"{animal} is {color}")
        else:
            print(f"{animal} is {color}")

#----------
#exercises
#----------

#ex 1
def my_func(nums):
    
    if nums == 0 or nums == 1:
        if nums == 0:
            print(f"number = 0")
        else:
            print(f"number = 1")
    elif nums % 2 == 0:
        print(f"{nums} is even")
    else:
        print(f"{nums} is odd")

#nums = int(input("write your number:"))
#my_func(nums)

#ex 2
my_func(33)

#ex 3
x = 55
if x > 13:
    print("x больше 13")
elif x > 51:
    print("x больше 51")
else:
    print("x меньше или равно 51")

#ex 4
for i in range(1, 6, 2):
    print(i)

num = 0
while num < 6:
    print(num)
    num += 2

#ex 5
sum = 0
for i in range(13, 0,-1):
    sum += i

print(sum)

#ex 6
i = 1
fact = 1
while i <= 6:
    fact *= i
    i += 1
print(fact)

#ex 7
for i in range(1, 10, 1):
    if i == 1:
        continue
    elif i == 2:
        pass
    elif i == 9:
        break
    else:
        print(i)

#ex 8
for i in range(3, 8):
    if i % 2 == 0:
        continue
    print(i)

#ex 9
for i in range(1, 21, 1):
    for j in range(1, 21, 1):
        print(i*j)

#ex 10
x = 0
while x < 6:
    y = 0
    while y < 3:
        print(f"x: {x}, y: {y}")
        y += 1
    x += 1
