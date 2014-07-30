# LPTHW Exercise 16 -- Reading and Writing Files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want to do that, hit RETURN."

raw_input("?")

print "Opening the file..."
#target = open(filename, 'w')
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
target.truncate(15)

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line4: ")

print "Now I'm going to write these to the file."

#target.write(line1)
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')
target.write('%r\n%r\n%r\n' % (line1, line2, line3))

print "And finally, we close it."
target.close()

