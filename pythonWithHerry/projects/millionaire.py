questions =[
  [
  "Who is Shah Rukh Khan?","WWE Wrestle", "Actor","Plumber","Doctor","Footballer",2],
  [
  "What is the Capital of France","Paris","Romo","London",0
  ],
  [
  "What is the Largest animal ? ", "Shark", "Blue Whale", "Elephant", "Giraffe", 2
  ],

  [
     "What is the square root of 64 ? ", "4", "8", "6", "2", 1
  ]  
  ]


for i in questions:
  print(i[0])
  print(f"Queston 1: {i[1]}")
  print(f"Queston 1: {i[2]}")
  print(f"Queston 1: {i[3]}")

  #check the answer is correct or not
  answer = int(input("Enter your answer: 1 for a, 2 for b, and 3 for c"))
  if answer == i[5]:
    print("Correct")