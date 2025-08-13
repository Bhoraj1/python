class Employee():
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def __str__(self):  #	Human-readable
    return f"Employee{self.name} earns {self.salary}"
  
  def __repr__(self):  # Developer-readable
    return f"Employee('{self.name}', {self.salary})"
  
  def __len__(self):
    return len(self.name)

e = Employee("John Doe", 10000)
print(str(e))
print(repr(e))  
print(len(e))  