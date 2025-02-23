import argparse

parser=argparse.ArgumentParser(description="A simple cmd argument parser")

#add parser
parser.add_argument("--name",type=str,help="Your name",required=True)
parser.add_argument("--age",type=int,help="Your age",required=True)
parser.add_argument("--greeting",type=str,help="Your greeting",default="Hello")

args=parser.parse_args()

print(f"{args.greeting} {args.name} You are {args.age} years old")
