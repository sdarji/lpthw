# LPTHW Exercise 19 -- Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)


print "Or we can use variables from our script."
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# add my own function, and call it 10 different ways
def adds_two(num):
    print "Your number (%d) plus two equals %d" % (num, num + 2)
my_num = 77
    
adds_two(4)
adds_two(15)
adds_two(9 + 123)
adds_two(my_num)
adds_two(my_num + 25)
adds_two(25 * my_num)
adds_two(my_num % 20)
adds_two(float(my_num) + 2.0)
adds_two(float(my_num) / 2.0)
adds_two(my_num if my_num > amount_of_cheese else amount_of_cheese)
adds_two(int(raw_input('type a number: ')))
