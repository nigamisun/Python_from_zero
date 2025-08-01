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
