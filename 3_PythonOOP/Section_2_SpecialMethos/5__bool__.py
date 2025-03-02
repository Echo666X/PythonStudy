# in this tutorial, you will learn how to implement the Python __bool__ method to return boolean values for objects of a custom class.

# an object of a custom class is associated with a boolean value, by default, it evaluates to True
# to override this default behavior, you implement the __bool__special method, the __bool__ method must return a boolean value
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True


if __name__ == '__main__':
    person = Person('Jane', 16)
    print(bool(person))  # False

# if a custom class doesn't have the __bool__ method, python will look for the __len__() method, if the __len__ is zero, the object is false, otherwise it is True
# If a class doesn’t implement the __bool__ and __len__ methods, the objects of the class will evaluate to True.

# The following defines a Payroll class that doesn’t implement __bool__ but the __len__ method:
class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print('len was called...')
        return self.length


if __name__ == '__main__':
    payroll = Payroll(0)
    print(bool(payroll))  # False

    payroll.length = 10
    print(bool(payroll))  # True