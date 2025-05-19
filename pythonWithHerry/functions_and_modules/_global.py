def sum(a,b):
  c = a + b
  
  global z  #please modify global z
  z = 7 #This will refer to global z and not create a local varible
  return c

z = 10
print(sum(1,1))
print(z)