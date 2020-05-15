# Calling a Function

# Function definition is below : need to have 2 blank line


def printme(str):
    print(str)
    return


# Now you can call printme function
printme("Im first call to user defined function")
printme("Again second call to the same function")

# ----------------------------------------------------------------------------------------------------------------------

# Pass by reference vs value


def changeme(mylist):
    mylist.append([1, 2, 3, 4, 5, 6, 7])
    print("values inside the function ", mylist)
    return


mylist = [10, 20, 30]
print(mylist)
changeme(mylist)
print("values outside the function ", mylist)

# [10, 20, 30]
# values inside the function  [10, 20, 30, [1, 2, 3, 4, 5, 6, 7]]
# values outside the function  [10, 20, 30, [1, 2, 3, 4, 5, 6, 7]]


def changeme(mylist):
    mylist = [1, 2, 3, 4, 5, 6, 7]
    print("values inside the function ", mylist)
    return


mylist = [10, 20, 30]
print(mylist)
changeme(mylist)
print("values outside the function ", mylist)
# [10, 20, 30]
# values inside the function  [1, 2, 3, 4, 5, 6, 7]
# values outside the function  [10, 20, 30]
# ----------------------------------------------------------------------------------------------------------------------

# Function Arguments