from argparse import ArgumentParser

parser = ArgumentParser(description="Adds two numbers.")
parser.add_argument("num1", type=float)
parser.add_argument("num2", type=float)

args = parser.parse_args()


result = args.num1 + args.num2

print(result)