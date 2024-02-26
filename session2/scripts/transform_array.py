import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser(description="transform an array file.")
parser.add_argument("infile", type=str, help="an .npy file to work on.")
parser.add_argument("outfile", type=str, help="an .npy file to save.")
parser.add_argument("op", type=str, choices=['normalize', 'standardize'])

args = parser.parse_args()

input_array_path = args.infile
output_array_path = args.outfile

input_array = np.load(input_array_path)  # load the input

if args.op == "normalize":
    output_array = (input_array - np.min(input_array)) / np.max(output_array)
elif args.op == "standardize":
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)


# Save the standardized array
np.save(output_array_path, output_array)


