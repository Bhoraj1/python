# Basic code -----------------------------------------
# a = 4
# b = 2
# c = 3

# averate = (a + b + c)/3
# print(averate)

# a1 = 4
# b1 = 2
# c1 = 1

# averate = (a1 + b1 + c1)/3
# print(averate)

## only log value in function -------------------------
def average(a,b,c):
  d = (a + b + c)/3
  print(d)
  return d

ol = average(4,3,2)
print(ol)

## Return the value in function -------------------------
def average(a,b,c):
  d = (a + b + c)/3
  return d

ol = average(4,3,2)
print(ol)

