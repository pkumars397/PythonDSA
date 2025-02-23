#argparse
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("num1",type=int,help="First Name")
parser.add_argument("num2",type=int,help="Second number")
parser.add_argument("--operation",choices=['add','sub','mul','div'],default="add",help="operations to perform")
args=parser.parse_args()
 
if args.operation=="add":
  result=args.num1+args.num2
elif args.operation=="sub":
  result=args.num1+args.num2
elif args.operation=="muL":
  result=args.num1*args.num2
elif args.operation=="div":
   if args.num2==0:
     result="Error division by0"
   else:
     result=args.num1/args.num2
print(f"Result: {result}")
