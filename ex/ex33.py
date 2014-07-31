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

number_loop(21, 3)
number_loop(8, 2)
number_loop(4, 1)