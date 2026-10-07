# Accept a single filename as a command line argument (version B)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Read file line by line
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

# Output each line with 1% probability (random.random() < 0.01)
import random
try:
    with open(filename, 'r') as file:
        for line in file: # Preserve original line order
            if random.random() < 0.01:  # 1% probability
                print(line.strip()) # Print sampled lines to standard output

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

