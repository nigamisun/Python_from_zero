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