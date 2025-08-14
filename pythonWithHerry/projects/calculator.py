try:
  a = int(input("Enter a First Number: ")) 

  b = int(input("Enter a Second Number: "))

  print("What kind of operation do you want to perform. press + for addition\nPress - for subtraction\nPress / for division\nPress * for multipication")

  o = input("Enter a Operation: ")
  match o:
    case "+":
      print(f"The Result is:{a+b}")
    case "-":
      print(f"The Result is:{a-b}")
    case "/":
      print(f"The Result is:{a/b}")
    case "*":
      print(f"The Result is:{a*b}")
    case _:
      print("Enter a Valid Operation")

except Exception as f:
 print("Enter an Valid Number.")
