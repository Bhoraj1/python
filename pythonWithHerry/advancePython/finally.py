a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))

try:
  c = (a/b)
  print(c)

except Exception as e:
  print(e)

finally:
  print("This is finally block which always execute success or not")  
 


# # QA Queston:
# def divide(a,b):
#   try:
#     c = (a/b)
#     print(c)

#   except Exception as e:
#     print(e)

#   finally:
#     print("This is finally block which always execute success or not")  
 
 
# a = int(input("Enter a number 1 : "))
# b = int(input("Enter a number 2 : "))
# divide(a,b)

