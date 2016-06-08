from sys import argv

script, operation, number1, number2 = argv

x = float(number1)
y = float(number2)

if operation == "a":
    print "answer %s" %(x + y)
if operation == "s":
    print "answer %s" %(x - y)
elif operation == "m":
    print "answer %s" %(x * y)
elif operation == "d":
    print "answer %s" %(x / y)
else:
    print "Try again"
