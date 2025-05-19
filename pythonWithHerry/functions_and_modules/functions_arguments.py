#Type of arguments
#1 Positional arguments
def add(a,b,plus=4):  # a and b are parameters. plus=4 is a default argumetns
  return a + b + plus

c = add(3,5)  #3,5 are argumetns
print(c)

#2 Default arguments
def add(a,b):  
  return a + b
c = add(b=3,a =5) 
print(c)