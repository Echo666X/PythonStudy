# in this tutorial, you’ll learn about Python methods and the differences between functions and methods.

# introduction to the python methods
# by definition, a method is a function that is buond to an instance of a class, this tutorial helps you understand how it works under the hood

class Request:
    def send():
        ''' test function'''
        print('Sent')
        
# and you can call the send() function via the Request class like this:
Request.send()
# the send() is a function object, which is an instance of the function class as shown in the following output
print(Request.send)
# the type of it is a function:
print(type(Request.send))
# now create a object of the Request class:
http_request = Request()
print(http_request.send) # it will return a bound method object
# so the http_request.send is not a function like the Request.send
print(http_request.send is Request.send ) # the output is false

# so, when you define a function inside a class, it's purely a function, however, when you access that function via an object, the function becomes a method
# therefore, a method is a function() that is bound to an instance of a class

# if you call the send() function via the http_request object, you will get a TypeError
# because the http_request is a method that is bound to the http_request object, python always implicitly passes the object to the method as the first argument
class Request_1:
    def send(*args):
        print('Send',args)

Request_1.send() # the output is Send()
# however, if you call the send function from an instance of the Request class, the args is not empty
http_request_1 = Request_1()
http_request_1.send() # in this case, the send() method receives an object which is the http_request, which is the object that it is bound to.

# in the other word, you can access the instance of the class as the first argument inside the send() method:
http_request_1.send()
# is equivalent to:
Request_1.send(http_request_1)


# for this reason, a method of an object always has the object as the first argument, by convention, it is called self:
class Request_2:
    def send(self):
        print('send',self)
        print('send')
        
http_request_2 = Request_2()
http_request_2.send()