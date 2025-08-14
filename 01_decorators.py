#Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function.

def decorator(func):
    def Rapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return Rapper  

@decorator  
def say_hello():
    print("Hello")

say_hello() 
# a = decorator(say_hello)
# a()

'''
a will look something like this
def a()
    print("I am about to execute a function...")
    print("Hello")
    print("I have executed this function....")
'''
