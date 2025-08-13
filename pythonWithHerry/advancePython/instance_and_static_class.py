# class Employee():
#   company = "HP"
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

#   #Instance method(default)
#   def print_info(self):
#    return f"{self.name} earns {self.salary}"
  
#   #static method
#   @staticmethod
#   def sum(a,b):
#     return a + b
  
# e = Employee("John Doe", 10000) 
# print(e.sum(10,12))

# print(e.print_info())  
    

  #class method :class methods are usually used on the class itself rather than on an object.

#   @classmethod
#   def print_company(cls):
#      return cls.company
  
#   #class method
#   @classmethod
#   def change_company(cls,new_company):
#       cls.company = new_company

  
# e = Employee("John Doe", 10000) 

# # print(e.print_info())

# print(e.sum(10, 20)) #error will say 3 argumetns are given because it take self and to solve it i have to use like this :sum(self,a,b)

# # print(e.print_company())
# e.change_company("Dell")
# print(e.company)