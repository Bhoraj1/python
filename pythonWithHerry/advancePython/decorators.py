# Decorators is a function that take function, it creates a new function inside its body (wrapper). then it returns new function 

def  decorator(fun):
     def wrapper():
          print("Before text")
          fun()
          print("After text")
     return wrapper

@decorator
def  say_hello():
     print("Hello")

say_hello()