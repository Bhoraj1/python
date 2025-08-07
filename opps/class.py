# Class : Class is an blueprint or a template. Eg.Form for an exam that contains name,age,electives,father's name etc. It defines what an object will be like -what data will be hold and what action it can perform. It doesn't create the object itself, just the instructions for creating it.It like an Plan

# Object: Specific instance created form the template(class).Eg. Form which contains the data for John Doe 

class Employee:
  company = "Google"

  def  get_salary(self):
     return 34000
  

e1 = Employee() # an object of class Employee is created here
print(e1.get_salary())  # employee's get Salary method is called here


e2 = Employee() # another object of class Employee is created here)
print(e2.get_salary()) # employee's get Salary method is called here)
print(e2.company) 