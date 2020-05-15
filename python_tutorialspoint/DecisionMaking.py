# If
var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
print("bye")

# 1 - Got a true expression value
# 100
# bye


# ---------------------------------------------------------------------------------------------

# If Else
var1 = 700
if var1 == 100:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("1 - Got a false expression value")
    print(var1)
print("bye")

# 1 - Got a false expression value
# 700
# bye

# ---------------------------------------------------------------------------------------------

# If Elif Else
var = 100
if var == 200:
    print("1 - Got a false expression value")
    print(var)
elif var == 100:
    print("1 - Got a true expression value")
    print(var)
else:
    print("1 - Got a false expression value")
    print(var)
print("bye")

# 1 - Got a true expression value
# 100
# bye

# ---------------------------------------------------------------------------------------------

# Nested If
var = 100
if var < 200:
    print("value is less than 200")
    if var == 150:
        print("which is 150")
    elif var == 100:
        print("which is 100")
    elif var < 50:
        print("which is less than 50")
else:
    print("Could not be determined")
print("bye")

# value is less than 200
# which is 100
# bye
