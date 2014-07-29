# LPTHW Exercise 5 -- More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # cm
weight = 180 / 2.2 # kgs
eyes = 'Blue\\'
teeth = 'White'
hair = 'Brown\\'
num_teeth = 'two'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His %r teeth are usually %s depending on the coffee." % (num_teeth, teeth)

# this line is tricky, try to get it exactly right
print('If I add %d, %d, and %d, I get %d.' % (age, height, 
      weight, age + height + weight))