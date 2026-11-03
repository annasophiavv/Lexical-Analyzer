#this will be the entry point of the program.
#reads a file and calls functions in other files.
import sys

filename = sys.argv[1] #example command: python3 main.py sample.clite. filename will equal sample.clite

#open file with read only permissions, source is a string with the file's content
with open(filename, "r") as file:
    source = file.read()

print(source)