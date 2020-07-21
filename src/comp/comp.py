# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return F"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Starts with D:")

a = []

for human in humans:
    if(human.name[0] == 'D'):
        a.append(human.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")

b = []

for human in humans:
    if(human.name[-1] == 'e'):
        b.append(human.name)

print(b)

# # Write a list comprehension that creates a list of names of everyone
# # whose name starts with any letter between 'C' and 'G' inclusive.

import string

alphabet = string.ascii_uppercase
alphaC2G = alphabet[2:7]

print("Starts between C and G, inclusive:")

c = []

for human in humans:

    for letter in alphaC2G:
        if(human.name[0] == letter):
            c.append(human.name)

print(c)

# # Write a list comprehension that creates a list of all the ages plus 10.

print("Ages plus 10:")

d = []

for human in humans:
    if(human.age > 9):
        new_age = human.age
        new_age += 10
        d.append(new_age)

print(d)

# # Write a list comprehension that creates a list of strings which are the name
# # joined to the age with a hyphen, for example "David-31", for all humans.

print("Name hyphen age:")

e = []

for human in humans:
    e.append(F"{human.name}-{human.age}")

print(e)

# # Write a list comprehension that creates a list of tuples containing name and
# # age, for example ("David", 31), for everyone between the ages of 27 and 32,
# # inclusive.

print("Names and ages between 27 and 32:")

f = []

for human in humans:
    for i in range(27,33):
        if(human.age == i):
            f.append((F"{human.name}", human.age))

print(f)

# # Write a list comprehension that creates a list of new Humans like the old
# # list, except with all the names uppercase and the ages with 5 added to them.
# # The "humans" list should be unmodified.

print("All names uppercase:")

g = []

for human in humans:
    h_age = human.age
    h_age += 5
    g.append(F"('{human.name.upper()}', {h_age})")

print(g)

# Write a list comprehension that contains the square root of all the ages.

print("Square root of ages:")

import math

h = []

for n in humans:
    h.append(math.sqrt(n.age))

print(h)
