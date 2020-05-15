# For
for letter in 'Python':
    print('letter in ', letter)
# letter in  P
# letter in  y
# letter in  t
# letter in  h
# letter in  o
# letter in  n
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('current fruit ', fruit)
print("bye")
# current fruit  banana
# current fruit  apple
# current fruit  mango
# bye

# ---------------------------------------------------------------------------------------------

# Iterating by Sequence Index
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('current fruit ', fruits[index])
print("bye")
# current fruit  banana
# current fruit  apple
# current fruit  mango
# bye

# ---------------------------------------------------------------------------------------------

# To prove whether a number is a prime number,
# first try dividing it by 2, and see if you get a whole number.
# If you do, it can't be a prime number.
# If you don't get a whole number,
# next try dividing it by prime numbers: 3, 5, 7, 11 (9 is divisible by 3) and so on,
# always dividing by a prime number

# Using Else with For
for num in range(10, 20):  # num will start @ 10
    for i in range(2, num):  # i will start @ 2
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, i, j))
            break
    else:
        print(num, 'is a prime')
# 10 equals 2 * 5
# 11 is a prime
# 12 equals 2 * 6
# 13 is a prime
# 14 equals 2 * 7
# 15 equals 3 * 5
# 16 equals 2 * 8
# 17 is a prime
# 18 equals 2 * 9
# 19 is a prime

# ---------------------------------------------------------------------------------------------

# While
count = 0
while count < 9:
    print("count is : ", count)
    count = count + 1
print("bye")
# count is :  0
# count is :  1
# count is :  2
# count is :  3
# count is :  4
# count is :  5
# count is :  6
# count is :  7
# count is :  8
# bye

# ---------------------------------------------------------------------------------------------

# While with Else
count = 0
while count < 9:
    print("count is : ", count)
    count = count + 1
else:
    print(count, " is not less than 9 ", )
print("bye")
# count is :  0
# count is :  1
# count is :  2
# count is :  3
# count is :  4
# count is :  5
# count is :  6
# count is :  7
# count is :  8
# 9  is not less than 9
# bye

# ---------------------------------------------------------------------------------------------

# Nested While loop - determine prime numbers

# To prove whether a number is a prime number,
# first try dividing it by 2, and see if you get a whole number.
# If you do, it can't be a prime number.
# If you don't get a whole number,
# next try dividing it by prime numbers: 3, 5, 7, 11 (9 is divisible by 3) and so on,
# always dividing by a prime number

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, ' is prime')
    i = i + 1
print("bye")

# 2  is prime
# 3  is prime
# 5  is prime
# 7  is prime
# 11  is prime
# 13  is prime
# 17  is prime
# 19  is prime
# 23  is prime
# 29  is prime
# 31  is prime
# 37  is prime
# 41  is prime
# 43  is prime
# 47  is prime
# 53  is prime
# 59  is prime
# 61  is prime
# 67  is prime
# 71  is prime
# 73  is prime
# 79  is prime
# 83  is prime
# 89  is prime
# 97  is prime
# bye

# ---------------------------------------------------------------------------------------------

# Infinite loop
# flag = 1
# while flag:
#     print('Given flag is really true!')
# print("Good bye!")
#
# # Given flag is really true!
# # Given flag is really true!
# # Given flag is really true!
# # Given flag is really true!
# # Given flag is really true!
# # Given flag is really true!
# # Given flag is really true!
# # Process finished with exit code -1
#
# # need to click stop button

# ---------------------------------------------------------------------------------------------

# Loop Control Statement

# Break
for letter in 'Python':
    if letter == 'h':
        break
    print('current letter ', letter)

var = 10
while var > 0:
    print('current var ', var)
    var = var - 1
    if var == 5:
        break
print("bye")

# current letter  P
# current letter  y
# current letter  t
# current var  10
# current var  9
# current var  8
# current var  7
# current var  6
# bye

# ---------------------------------------------------------------------------------------------

# Continue
for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")

# Current Letter : P
# Current Letter : y
# Current Letter : t
# Current Letter : o
# Current Letter : n
# Current variable value : 9
# Current variable value : 8
# Current variable value : 7
# Current variable value : 6
# Current variable value : 4
# Current variable value : 3
# Current variable value : 2
# Current variable value : 1
# Current variable value : 0
# Good bye!

# ---------------------------------------------------------------------------------------------

for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print ('Current Letter :', letter)
print("Good bye!")

# Current Letter : P
# Current Letter : y
# Current Letter : t
# This is pass block
# Current Letter : h
# Current Letter : o
# Current Letter : n
# Good bye!
