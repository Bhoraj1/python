# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

#   def fname(self):
#       return self.name.split(" ")[0]
    

# e = Employee("John Doe", 10000)
# print(e.fname())


class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @property
  def fname(self):
      return self.name.split(" ")[0]
    
  @fname.setter
  def fname(self, newFname): 
       parts = self.name.split(" ")
       self.name = f"{newFname} {parts[1]}"

e = Employee("John Doe Ram", 10000)
e.fname = "Ram"
print(e.name)  

