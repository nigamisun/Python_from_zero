#-----------
#Chapter 5: Data structures: Lists, Tuples and Dictionaries.
#-----------

#List[] — an ordered collection of elements, represented by square brackets [].
#Tuple() — an ordered, immutable collection of elements, represented by parentheses ().
#Dictionary{} — an unordered collection of key-value pairs, represented by curly braces {}.
#Set{} — an unordered collection of unique elements, also represented by curly braces {}.

numbersl = [1, 2, 3, 5, 5]
numbersl.append(0)
print(numbersl)

print(numbersl[-2])
print(numbersl[4])

numbers = (1, 5, 2, 2, 7, 3)

print(numbers[3])
print(numbers[-3])
sorted_numbers = sorted(numbers)
print(sorted_numbers)

ages = {"Gector":42, "John":35, "Samuel":19}
print(ages["John"])
print(ages.get("Anna", 38))
ages["Anna"] = 38
print(ages)

doubles = [num*2 for num in numbers]
print(doubles)

doublesl = [x*2 for x in numbersl]
print(doublesl)

odds = [num + 1 for num in doubles if (num + 1) % 2 != 0]
print(odds)

evensl = [x for x in doublesl if x % 2 == 0]
print(evensl)

evensl.sort()
print(evensl)
odds.sort(reverse = True)
print(odds)

if 3 in odds:
    print("3 is in the odds")
else:
    pass

if "Anna" in ages:
    print(ages["Anna"])
else:
    pass

nums = [4, 5, 6, 2, 8, 1, 2, 3,]
colors = ["green", "red", "blue", "white", "black"]
copy = nums.copy()
clone = nums[:]
sliced_nums = nums[1:4]
sliced_nums_re = nums[-6:-2]
sliced_nums_st = nums[0:6:2]
sliced_nums_st_re = nums[-6:-1:2]
pairs = [(n, c) for n in nums for c in colors]
pairs_p = list(zip(nums, colors))

import itertools as it
pairs_p_c = list(zip(nums, it.cycle(colors)))

print(copy)
print(clone)
print(sliced_nums)
print(sliced_nums_re)
print(sliced_nums_st)
print(sliced_nums_st_re)
print(pairs)
print(pairs_p)
print(pairs_p_c)

my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
new_dict = {k: v * v for k, v in my_dict.items() if v > 1 and v < 7}
print(new_dict)

my_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
my_dict_1 = {k: v for k, v in my_list}
print(my_dict_1)

new_dict_z = {n: c for n, c in zip(nums, colors)}
print(new_dict_z)
new_dict_d = dict(zip(nums, colors))
print(new_dict_d)

my_set = set(colors)
num_set = set(nums)

union_set = my_set | num_set        
union_set1 = my_set.union(num_set)

num = set(numbers)
numl = set(numbersl)
numl.add(9)
inter = num & numl
inter1 = num.intersection(numl)
difer = num - numl
difer_re = numl - num
difer1 = num.difference(numl)
sym_difer = num ^ numl
sym_difer1 = num.symmetric_difference(numl)


print(my_set)
print(num_set)
print(union_set)
print(union_set1)
print(num)
print(numl)
print(inter)
print(inter1)
print(difer)
print(difer1)
print(difer_re)
print(sym_difer)
print(sym_difer1)

numl.discard(9)
print(numl)
num.remove(5)
print(num)

my_stack1 = []
my_stack1.append(1)
my_stack1.append(2)
my_stack1.append(3)
print(my_stack1)
my_stack1.pop()
print(my_stack1)

my_queue1 = []
my_queue1.append(1)
my_queue1.append(2)
my_queue1.append(3)
my_queue1.append(4)
print(my_queue1)
my_queue1.pop(0)
print(my_queue1)

my_list2 = [{'name': 'Azamat', 'age': 26}, {'name': 'Raul', 'age': 12},
{'name': 'John', 'age': 52}, {'name': 'Tyson', 'age': 60}]
sorted_list2 = sorted(my_list2, key=lambda x: x['age'])
print(sorted_list2)

my_list = ['Peter', 'robot', 'Ivan', 'Sergey']
my_list.sort(key=lambda x: x.lower())
print(my_list)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = binary_search(arr, 5)
print("result: ", res)

import searcher 

cnums = {6, 3, 18, -1, 8, 4, 2, 9, 5, 7, 0}
cnumk = (6, 3, 18, -1, 8, 4, 2, 9, 5, 7, 0)
cnuml = [6, 3, 18, -1, 8, 4, 2, 9, 5, 7, 0]

b_searchs = searcher.Sort_Search(cnums)
b_searchk = searcher.Sort_Search(cnumk)
b_searchl = searcher.Sort_Search(cnuml)

print("b_searchs: ", b_searchs.binary_search(6))
print("b_searchk: ", b_searchk.binary_search(18))
print("b_searchl: ", b_searchl.binary_search(0))


my_list = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
element = my_list[0][2]
print(element)

my_dict = {'a': {'b': {'c': 3}}, 'd': 1}
def process_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            process_dict(v)
        else:
            print(k, v)

process_dict(my_dict)

#----------
#exercises
#----------

#ex 1
list_ex = [1, 3, 4, 6, 2, 7, 0, 2]
tuple_ex = (1, 3, 4, 6, 2, 7, 0, 2)
dict_ex = {'a':1, 'b':2, 'c':3, 'd':4}

#ex 2
fruits = ["strawberry", "apricot", "orange", "grape"]
fruits.append("apple")
print(fruits)

#ex 3
coordinates = (3, 5, 6)
x, y, z = coordinates
print(f"x = {x} \ny = {y} \nz = {z}")

#ex 4
person = {"name" : "Peter", 
          "age" : 42, 
          "city" : "New Haven"}
person["city"] = "New York"
print(person)

#ex 5
squares_list = [x**2 for x in range(8, 0, -1)]
print(squares_list)

#ex 6
numbers_ex = [4, 8, 5, 1, 9, 7, 2, 3, 0]
numbers_ex_s = sorted(numbers_ex)
print(numbers_ex_s)

#ex 7
sublist = [numbers_ex[6], numbers_ex[8], numbers_ex[7]]
print(sublist)

#ex 8
squares_dict = {x: x**2 for x in range(10, 0, -1)}
print(squares_dict)

#ex 9 
A = {5, 4, 3, 2, 1} 
B = {7, 8, 6, 5, 4}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)

#ex 10
matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(matrix)

element = matrix[1][1]
print(element)

flat = [i for row in matrix for i in row]
print("Объединённый список:", flat)
