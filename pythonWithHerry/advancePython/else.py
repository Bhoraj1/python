try:
  a = 454/0
  print(a)
except Exception as e:
  print(e)

#if there is no error in try block then else will be executed.
else:
  print("This will run only if except is not running")  