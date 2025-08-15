questions =[
  [
  "Who is Shah Rukh Khan?","WWE Wrestle", "Actor","Plumber","Doctor",2],
  [
  "What is the Capital of France","Paris","Romo","London","New work",1
  ],
  [
  "What is the Largest animal ? ", "Shark", "Blue Whale", "Elephant", "Giraffe", 1
  ],
  [
     "What is the square root of 64 ? ", "4", "8", "6", "2", 2
  ]  
  ]



for i in questions:
  print(i[0])
  print(f"a : {i[1]}")
  print(f"b : {i[2]}")
  print(f"c:  {i[3]}")
  print(f"d : {i[4]}")


  #check the answer is correct or not
  a = answer = int(input("Enter your answer: a:1 , b:2 , c:3 , D:4 "))
  if (i[5] == a):
    print("Correct")
  else:
    print(f"Incorrect, The answer was {i[5]}") 
