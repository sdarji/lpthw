# LPTHW Exercise 33 -- While-Loops

def number_loop(num, increment):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num,

def number_loop_2(num, increment):
    numbers = [i for i in range(0, num, increment)]
    print '\n\nThis is the Pythonic way:\n%r' % numbers

number_loop(21, 3)
number_loop_2(24, 2)