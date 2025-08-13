import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int, help="Enter the first number")
parser.add_argument("num2", type=int, help="Enter the second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Enter the operation")

args = parser.parse_args()

if(args.operation =="add"):
    print(args.num1 + args.num2)

elif(args.operation =="sub"):
    print(args.num1 - args.num2)

elif(args.operation =="div"):
    print(args.num1 / args.num2)
    
elif(args.operation =="mul"):
    print(args.num1 * args.num2)

else:
    print("Invalid operation")

    

