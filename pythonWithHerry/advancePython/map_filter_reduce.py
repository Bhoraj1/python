# #map,filter and Reduce

# #map---------
# numbers = [1,24,64,75,33]

# def squares(x):
#    return x*x


# # new = map(squares,numbers)
# new = map(lambda x: x*x, numbers) # also used lamda commanly espically for one line
# print(list(new))




#filter ---------------

# a = [2,54,65,76,32,57,43,76,78,98]
# def greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False

# # new = filter(lambda x: x>9, a) # also where we can also use lamda
# new = filter(greater_than_9,a)
# print(list(new))

#reducer ---------------
from functools import reduce
numbers = [1,2,3,4,5,6,7]
     # [3,3,4,5,6,7]
     # [6,4,5,6,7]
     # [10,5,6,7]
     # [15,6,7]
     # [21,7]
     # [28]


def sum(a,b):
     return a+b

c = reduce(sum, numbers)
print(c)