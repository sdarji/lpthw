# LPTHW Exercise 20 -- Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print "Now let's rewind again."
rewind(current_file)

new_line = int(raw_input("Now enter a character number to start from: "))
current_file.seek(new_line - 1)

print "Let's print the next two lines from your character #."
print_a_line(1, current_file)
print_a_line(2, current_file)

current_file.close()