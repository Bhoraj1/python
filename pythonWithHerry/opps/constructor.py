# A constructor is a special function in a class that runs automatically when you create (instance) an object from that class.

class Employee:  
  def __init__(self,salary,name,bond): 
      self.salary = salary
      self.name = name
      self.bond = bond

  def get_salary(self):
     print(f"Name: {self.name}, Salary: {self.salary}")
  

e1 = Employee(4000,"Johan Doe",4) 
e2 = Employee(4000,"Johan",4) 
e1.get_salary()  
e2.get_salary() 


