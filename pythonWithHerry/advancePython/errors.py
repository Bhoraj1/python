try:
    a = int(input("Enter a number 1 : "))
    b = int(input("Enter a number 2 : "))

    print(f"The Sum is {a + b}") 

  #  except:
  #     print("Please enter a valid number")  
except Exception as e:
      print(e)  
      



while True:
   try:
    a = int(input("Enter a number 1 : "))
    b = int(input("Enter a number 2 : "))

    print(f"The Sum is {a + b}") 

   except ValueError:
      print("Please enter a valid number")

   except ZeroDivisionError:
      print("Please enter a number greater than 0")    

  #  except:
  #     print("Please enter a valid number")  
   
   except Exception as e:
      print("Unknown Error Occured",e)  



# a = int(input("Enter a number 1 : "))
# b = int(input("Enter a number 2 : "))

# if b == 0: #raise means: "Stop the program right here and throw an error."
#   raise ValueError("b cannot be zero")
# print(f"The Sum is {a + b}") 
