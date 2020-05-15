print("Hello, World!")
# Hello, World!

# ---------------------------------------------------------------------------------------

# assigning values
counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string

print(counter)
print(miles)
print(name)
# 100
# 1000.0
# John

# ---------------------------------------------------------------------------------------

# Multiple Assignment
a = b = c = 1
print(a)  # 1
print(b)  # 1
print(c)  # 1

a, b, c = 1, 2, "john"
print(a)  # 1
print(b)  # 2
print(c)  # john

# ---------------------------------------------------------------------------------------

# Standard Data Types
# Python has five standard data types −
#
#     Numbers
#     String
#     List
#     Tuple
#     Dictionary

# ---------------------------------------------------------------------------------------

# Python Strings
str = "Hello World!"

print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + " TEST")

# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World! TEST

# ---------------------------------------------------------------------------------------

# Python Lists

list = ['abcd', 768, 2.23, 'john', 70.2]
tinyList = [123, 'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinyList * 2)
print(list + tinyList)

# ['abcd', 768, 2.23, 'john', 70.2]
# abcd
# [768, 2.23]
# [2.23, 'john', 70.2]
# [123, 'john', 123, 'john']
# ['abcd', 768, 2.23, 'john', 70.2, 123, 'john']

# ---------------------------------------------------------------------------------------

# Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
# This is one
# This is two
# {'name': 'john', 'code': 6734, 'dept': 'sales'}
# dict_keys(['name', 'code', 'dept'])
# dict_values(['john', 6734, 'sales'])

# ---------------------------------------------------------------------------------------


