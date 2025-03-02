# in this tutorial, you will learn about the python __del__ special method and understand how it works

# In Python, the garbage collector manages memory automatically. The garbage collector will destroy the objects that are not referenced.
# If an object implements the __del__ method, Python calls the __del__ method right before the garbage collector destroys the object.
# However, the garbage collector determines when to destroy the object. Therefore, it determines when the __del__ method will be called.
# The __del__ is sometimes referred to as a class finalizer. Note that __del__ is not the destructor because the garbage collector destroys the object, not the __del__ method.
# The Python __del__ pitfalls
# Python calls the __del__ method when all object references are gone. And you cannot control it in most cases.
# Therefore, you should not use the __del__ method to clean up the resources. It’s recommended to use the context manager.
# If the __del__ contains references to objects, the garbage collector will also destroy these objects when the __del__ is called.
# If the __del__ references the global objects, it may create unexpected behaviors.
# If an exception occurs inside the __del__ method, Python does not raise the exception but keeps it silent.
# Also, Python sends the exception message to the stderr. Therefore, the main program will be able to be aware of the exceptions during the finalization.
# In practice, you’ll rarely use the __del__ method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


if __name__ == '__main__':
    person = Person('John Doe', 23)
    person = None #None is one of Python's built-in constants, and its type is NoneType, which means "no value" or "empty".
# when we set the person object to None, the garbage collector dwstorys it because there is no reference, therefore, the __del__ method was called

# if you use the del keyword to delete the person object, the __del__ method is also called

person1 = Person('John Doe', 23)
del person1