print("python is really a great language,", "isn't it?")
# python is really a great language, isn't it?

# ----------------------------------------------------------------------------------------------------------------------

# The input Function

str = input("enter your input: ")
print("your input is : ", str)
# enter your input: raw_input not working
# your input is :  raw_input not working

# ----------------------------------------------------------------------------------------------------------------------

# The open() Method

# wb
# Opens a file for writing only in binary format.
# Overwrites the file if the file exists.
# If the file does not exist, creates a new file for writing.

fo = open("foo.txt", "wb")
print("file name : ", fo.name)
print("file is close : ", fo.closed)
print("file opening mode : ", fo.mode)

# your input is :  fd
# file name :  foo.txt
# file is close :  False
# file opening mode :  wb
# foo.txt is created on the same directory level

# ----------------------------------------------------------------------------------------------------------------------

# The write() Method

# w
# Opens a file for writing only.
# Overwrites the file if the file exists.
# If the file does not exist, creates a new file for writing.

fo = open("foo1.txt", "w")
fo.write("python is a great programming languae.\n yeah its great!!!\n")

# foo1.txt is created on the same directory level
# with content :
# python is a great programming languae.
#  yeah its great!!!

# ----------------------------------------------------------------------------------------------------------------------

# The read() Method

# r+
# Opens a file for both reading and writing.
# The file pointer placed at the beginning of the file.

fo = open("foo1.txt", "r+")
str = fo.read()
print("read string is : ", str)
# read string is :  python is a great programming languae.
# yeah its great!!!

# The close() Method
fo.close()

fo = open("foo1.txt", "r+")
str = fo.read(10)
print("read string is : ", str)
# read string is :  python is

# The close() Method
fo.close()

# ----------------------------------------------------------------------------------------------------------------------

# still not complete

