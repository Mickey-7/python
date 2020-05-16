# Creating Classes


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("name : ", self.name, "\nsalary : ", self.salary)


emp1 = Employee("zara", 70000)
emp2 = Employee("zorro", 90000)

emp1.display_employee()
emp2.display_employee()

# name :  zara
# salary :  70000
# name :  zorro
# salary :  90000

# ---------------------------------------------------------------------------------------------------------------------------

# You can add, remove, or modify attributes of classes and objects at any time

emp2.age = 27
emp2.address = "USA"
print(hasattr(emp2, 'age'))
print(getattr(emp2, 'age'))
# True
# 27
print(hasattr(emp2, 'address'))
del emp2.address
print(hasattr(emp2, 'address'))
# True
#
# # False


# You can use the following functions −
# The getattr(obj, name[, default]) − to access the attribute of object.
# The hasattr(obj,name) − to check if an attribute exists or not.
# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# The delattr(obj, name) − to delete an attribute.

print(hasattr(emp1, 'age'))
setattr(emp1, 'age', 17)
print(getattr(emp1, 'age'))
delattr(emp1, 'age')
print(hasattr(emp1, 'age'))
# False
#
# 17
#
# False

# ---------------------------------------------------------------------------------------------------------------------------

